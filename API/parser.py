import json

from API.codedecode import CodeDecode


class Parser:
    decode = object()

    def __init__(self, os):
        self.decode = CodeDecode(os=os)

    def parse_dashboard(self, response):
        output = json.loads(response.content)
        all_posts = self.decode.decode_dictionary_list(output['174'])
        print("Dashboard Posts: \n-")
        for post in all_posts:
            print(">>>>", post, sep='\n- ')
        opportunities = self.decode.decode_dictionary_list(output['236'])
        print("Opportunities Cards: \n-")
        for oppo in opportunities:
            print(">>>>", oppo, sep='\n- ')
        recommended_posts = self.decode.decode_dictionary_list(output['367'])
        print("Recommended Posts: \n-")
        for rpost in recommended_posts:
            print(">>>>", rpost, sep='\n- ')
        recommended_profiles = self.decode.decode_dictionary_list(output['389'])
        print("Recommended Profiles: \n-")
        for rpro in recommended_profiles:
            print(">>>>", rpro, sep='\n- ')
        suggested_profiles = self.decode.decode_dictionary_list(output['390'])
        print("Suggested Profiles: \n-")
        for spro in suggested_profiles:
            print(">>>>", spro, sep='\n- ')

    #    for card in cards:
    #       print(decode_android_dictionary(card))

    def parse_dashboard_filter(self, response):
        output = json.loads(response.content)

        industries = self.decode.decode_list(output['167'])
        print("Industries: \n-")
        for industry in industries:
            print(">>>>", industry, sep='\n- ')
        targets = self.decode.decode_dictionary_list(output['173'])
        print("Targets: \n-")
        for target in targets:
            print(">>>>", target, sep='\n- ')
        offerings = self.decode.decode_dictionary_list(output['174'])
        print("Offerings: \n-")
        for offering in offerings:
            print(">>>>", offering, sep='\n- ')
        recommended_posts = self.decode.decode_dictionary_list(output['367'])
        print("Recommended Posts: \n-")
        for recommended_post in recommended_posts:
            print(">>>>", recommended_post, sep='\n- ')
