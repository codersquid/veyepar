#!/usr/bin/python

# mk_public.py - flip state on hosts from private to public
# private = not listed, can be seen if you know the url
#     the presenters have been emaild the URL, 
#     they are encouraged to advertise it.
# public = advertised, it is ready for the world to view.  
#     It will be tweeted at @NextDayVideo

from steve.richardapi import update_video, MissingRequiredData
from steve.restapi import API, get_content

import youtube_uploader

import gdata.youtube
from gdata.media import YOUTUBE_NAMESPACE
from atom import ExtensionElement
import atom

import pw

from process import process
import pprint

from main.models import Show, Location, Episode, Raw_File, Cut_List

class mk_public(process):

    ready_state = 9

    def up_richard(self, ep):

        host = pw.richard[ep.show.client.richard_id]
        endpoint = 'http://{hostname}/api/v1'.format(hostname=host['host'])
        api = API(endpoint)

        vid = ep.public_url.split('/video/')[1].split('/')[0]

        response = api.video(vid).get(
                username=host['user'], api_key=host['api_key'])

        video_data = get_content(response)
        video_data['state'] = 1

        try: 
            update_video(endpoint, host['user'], host['api_key'], 
                    vid, video_data)
        except MissingRequiredData, e:
            # this shouldn't happen, prolly debugging something.
            import code
            code.interact(local=locals())

        return True

    def up_youtube(self, ep):

        uploader = youtube_uploader.Uploader()
        uploader.user = ep.show.client.youtube_id
        return uploader.set_permission( ep.host_url )

    def process_ep(self, ep):
        if self.options.verbose: print ep.id, ep.name
        # set youtube to public
        # set richard state to live
 
        ret = True  # if something breaks, this will be false
        if ep.public_url:
            ret = ret and self.up_richard(ep)
            if self.options.verbose: print "Richard public."

        if ep.host_url:
            ret = ret and self.up_youtube(ep)
            if self.options.verbose: print "Youtube public."

        return ret

if __name__ == '__main__':
    p=mk_public()
    p.main()

