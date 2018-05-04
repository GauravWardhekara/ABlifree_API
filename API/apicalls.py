import requests
import API.constants

authcode = "XScUK8LVQzXNeX1BVpd7I0qm4J2_Kp8VxFtAmd7aqvnabPd4iLjdvX04ovz5S91me9vOcYxw3EWBBNSFCQzldLm_" \
           "SMITpl9lPMADdVH66_ieD0IglQlQrZVTmLs1VbsndOrj8NpqQMsvvZ52o9QnS1qAUfCrVttMGWdQOEaxwdnC5w2i" \
           "7SZLEuGac4FL4Ei_ZKFMdvhLmM6tYaZIYmSzNleWL7duSTEb0LF_qfXkyjz_gkVsywZhIlg2mCtrOi7wXqEgrqeV" \
           "CqlGCuuuVz4dsSmwPRcd_u5G3dKJc-ZvhQiEjNFL5ZFh_ReOqyetUZRz3TExGEXgA6cHmwTYa2m0lWA5OiOOewTg" \
           "sU3qTjfpWroWvjOccZPO5kHm1mLtL_j94kfdtGKBntwidaVWnc6fAUmXUHAEhUDq6GAV0U_OdBJxAn6T"


class Requests:
    def __init__(self):
        self.base_url = API.constants.staging_base_url

    # Get Dashboard filtered data.
    def get_dashboard_filter(self):
        api_url = self.base_url + API.constants.get_dashboard_filter
        headers = {'50': '0',
                   'Authorization': 'Bearer {0}'.format(
                       "GpGn9Rnm94b64VJ6yv9FGxBD1_zvrRvpNTI4ajujP8sGVc8GM0SwDgOFDu_M5VfuJ5ZbskTqH1ZSSwvjsO6Us_"
                       "2QsQLPpQfQZFzIec8nDRuio_fF-bAOU9F5OZX80X0bgwSVDqF0Kb3TqWgVPtkZyx-6ls-xQJ4a3sTYEDbBvZM_"
                       "kQpO8NksBfroazIW4vCXB-v3QUAw-GRvyAYMxHrTFbLT-4vpBxlMbzjeHdBh03lvekLJ2H7WRM81n0K2FIS8q"
                       "y8qHk4ylQ9Mv-k11injTkbMpPMuvFwInWLvXprNh5DRcTW5bMY4vNnVRwCSWwsQUpfPLuXt205014cuNmpBy"
                       "SkqnfPj5km_5VNWjKKfAOR5lkxPzGXLYN0FLHX1m5dLVE5MND_LfxSjmUsnI24mj5eyFUY5oDv9SzQ0uAa0GssDU_rO"),
                   '1': 'lBk4UvSqcNBoNhlSkmDtRQ==',
                   '191': 'HU8NXS4fdZMESgyQaGHpLg==',
                   '231': '9k36BzECdKGPIQ5RrnOoSeQia1c6jgylIb4p+Tb1CTQ='}
        target_area = "[{\"12\": \"3UmHSefHr52grBET9pglBw==\"," \
                      " \"13\": \"wjxYQ/xQbi3seel2yM7bTQ==\"," \
                      " \"14\": \"KDYDZmFPqD27XndAvCdCng==\"}," \
                      " {\"12\": \"3UmHSefHr52grBET9pglBw==\"," \
                      " \"13\": \"wjxYQ/xQbi3seel2yM7bTQ==\"," \
                      " \"14\": \"8c6gHIUk+99hTL4bZpxQmw==\"}]"
        industry = "[\"ApFEuzmNTFUStXCLEwiT1A==\", \"R/9PkDR6LhEmqrSdJ5HHsw==\"]"

        headers['166'] = str(target_area)
        headers['167'] = '{0}'.format(industry)
        response = requests.get(api_url, headers=headers)
        return response

    # Get Dashboard.
    def get_dashboard(self):
        api_url = self.base_url + API.constants.get_dashboard
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(
                       "UbwK3a7maX7Tfg42bkmKw2oKe9njKkNeVU-qvf-tLxnT09C61GOlzJZXXxwwCPp26BnuReFJwNgPBPvikt_"
                       "cmQhu2EbxkdQ4TRibO4QrCqcdsZTu-4hOQoouKj0_oGsIYdxlJPjqJIaKAr8yoYh2tiLi5yfz6xeBneOjnT-"
                       "RJN6fCYGvanvc0FfmpxoQ7A19hpL1olqdVvIfT7MjpHK0YoCLvwTF54QRjXJQddxcLEVOOoyZ9VycnvmZJz"
                       "ENA9mfUIFYzmRSJ0ZwIeSDipsRRfoQhcBhlJjaYckX_kqKLLwHOPtGxF-ixTE0FCB5yRvjSxGryoMK3AP2D"
                       "-5Lcs-Bpt6sO9N53dPaOGz7SygA22jrhygcB_QuPwGCrfA147yokkl5ZluisC9gylyRV6n9umeOGstZB"
                       "XsRYZotNNhHmzI3l97R"),
                   '1': 'PBW0sDeG2dE0Nc9GPkXyHg==',
                   '231': 'NpXDbn8SYDDzInCUiN1CoMDj3rMvKW7VhuVVIo4ul+Q=',
                   '12': 'LeTl76d9JOdpmtXNwtZlqg==',
                   '14': 'XPg6Coqs4KsgVTAAUsM3WA=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Suggested Profile list.
    def get_suggested_profiles(self):
        api_url = self.base_url + API.constants.get_suggested_profile
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'J1+uTW/L1L+b9YkQgbg2pg==',
                   '191': 'oTUe+HgPTltCQQRZJbc7Gw=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Set selected card as Primary card.
    def post_set_primary_card(self):
        api_url = self.base_url + API.constants.post_primary_card
        headers = {'50': '1',
                   'Authorization': 'Bearer ' + authcode,
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'J1+uTW/L1L+b9YkQgbg2pg==',
                   '191': 'oTUe+HgPTltCQQRZJbc7Gw=='}
        data = {'32': '7YNvp5+VYf64KuQ+Cg7UKQ=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Get list of cards with opportunities.
    def get_opportunities_card_list(self):
        api_url = self.base_url + API.constants.get_opportunity_card_list_v2
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'J1+uTW/L1L+b9YkQgbg2pg==',
                   '191': 'oTUe+HgPTltCQQRZJbc7Gw==',
                   '12': 'LeTl76d9JOdpmtXNwtZlqg ==',
                   '13': 'tbNulXc57SGOHLXhQNhAAQ ==',
                   '14': 'XPg6Coqs4KsgVTAAUsM3WA ==',
                   '161': 'PrW20A690udsFutIGhXF5w ==',
                   '162': 'tTWRsuYURj66ptxOPMCHOQ =='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Business Bit details.
    def get_business_bit_details(self):
        api_url = self.base_url + API.constants.get_business_bit_details
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '376': 'ZYYvOzNabKQcfFl5b9JMXQ=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get list tagging users.
    def get_user_tagging_list(self):
        api_url = self.base_url + API.constants.get_user_tagging_list
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Post Activity Log.
    def get_post_activity_log(self):
        api_url = self.base_url + API.constants.get_saved_posts_v3
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '376': 'ZYYvOzNabKQcfFl5b9JMXQ==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '32': 'pA1e7SmIwc9za5LS/zyRag=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Posts on a Card.
    def get_posts_on_card(self):
        api_url = self.base_url + API.constants.get_posts_on_card
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '32': 'pA1e7SmIwc9za5LS/zyRag=='}
        response = requests.get(api_url, headers=headers)
        return response

    # View Business Bit details.
    def post_view_business_bit_details(self):
        api_url = self.base_url + API.constants.post_view_business_bit
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'376': 'Rx0bxR9RetsFabsHveW7wA=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Upvote Business Bit details.
    def post_upvote_business_bit_details(self):
        api_url = self.base_url + API.constants.post_upvote_business_bit
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'376': 'Rx0bxR9RetsFabsHveW7wA=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Remove Upvote Business Bit details.
    def post_remove_upvote_business_bit_details(self):
        api_url = self.base_url + API.constants.post_remove_business_bit_upvote
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'376': 'Rx0bxR9RetsFabsHveW7wA=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Get Comments list on Business Bit.
    def get_user_comments_on_business_bit(self):
        api_url = self.base_url + API.constants.get_user_comments
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '376': 'ZYYvOzNabKQcfFl5b9JMXQ ==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw ==',
                   '191': 'HfHXvU6ExF63Ky8GwHrepw =='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Comments list on Requirement or Offering.
    def get_user_comments_on_requirement_offering(self):
        api_url = self.base_url + API.constants.get_user_comments
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '170': 'ZZoNwvOYPBr6dZn5qO0hQw==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw ==',
                   '191': 'jrTd1ZWCVIuE13sUpYXz1A=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Change Email(incomplete).
    def post_change_user_name(self):
        api_url = self.base_url + API.constants.get_user_comments
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '170': 'ZZoNwvOYPBr6dZn5qO0hQw==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw ==',
                   '191': 'jrTd1ZWCVIuE13sUpYXz1A=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Add business Bit.
    def post_add_business_bit(self):
        api_url = self.base_url + API.constants.post_create_business_bit
        headers = {
            '1': "cHB/sRc1aMRGSm8aHbRfpg==",
            '50': "1",
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer {0}".format(authcode),
        }
        data = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"32\"\r\n\r\npA1e7SmIwc9za5LS/zyRag==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"377\"\r\n\r\nMCGU0iALdcIILmWqsYeBXSjBfWguOtYHmvdsN414m/c=\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"12\"\r\n\r\nLeTl76d9JOdpmtXNwtZlqg==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:" \
               " form-data; name=\"13\"\r\n\r\ntbNulXc57SGOHLXhQNhAAQ==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"14\"\r\n\r\nXPg6Coqs4KsgVTAAUsM3WA==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
               "name=\"378\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:" \
               " form-data; name=\"379\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Update business Bit.
    def post_update_business_bit(self):
        api_url = self.base_url + API.constants.post_update_business_bit
        headers = {
            '1': "cHB/sRc1aMRGSm8aHbRfpg==",
            '50': "1",
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer {0}".format(authcode),
        }
        data = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"32\"\r\n\r\nu/GIuGjmfXImZQtM2F0imA==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"377\"\r\n\r\nMCGU0iALdcIILmWqsYeBXSjBfWguOtYHmvdsN414m/c=\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"12\"\r\n\r\nLeTl76d9JOdpmtXNwtZlqg==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"13\"\r\n\r\ntbNulXc57SGOHLXhQNhAAQ==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
               " name=\"14\"\r\n\r\nXPg6Coqs4KsgVTAAUsM3WA==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:" \
               " form-data; name=\"376\"\r\n\r\nFRdynsJjU83GvFUyXi/C6w==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:" \
               " form-data; name=\"383\"\r\n\r\nxP/TgU0592aK52UP85hEJA==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:" \
               " form-data; name=\"384\"\r\n\r\nxP/TgU0592aK52UP85hEJA==\r\n" \
               "------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Delete Business Bit.
    def post_delete_business_bit(self):
        api_url = self.base_url + API.constants.post_delete_business_bit
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'376': 'FRdynsJjU83GvFUyXi/C6w=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Add Comment on Business Bit.
    def post_comment_business_bit(self):
        api_url = self.base_url + API.constants.post_add_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'376': '5Sieb+BdtcXLRulTrrv+pg==',
                '32': 'pA1e7SmIwc9za5LS/zyRag==',
                '381': '5DQzfW8UIl63nhd0iBj003/rXbpd4YcM4dcTC/4G2J8=',
                '191': 'HfHXvU6ExF63Ky8GwHrepw=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Add Comment on Requirement or Offering.
    def post_comment_requirement_offering(self):
        api_url = self.base_url + API.constants.post_add_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'170': 'ZZoNwvOYPBr6dZn5qO0hQw==',
                '32': 'pA1e7SmIwc9za5LS/zyRag==',
                '381': '5DQzfW8UIl63nhd0iBj003/rXbpd4YcM4dcTC/4G2J8=',
                '191': 'jrTd1ZWCVIuE13sUpYXz1A=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Update Comment on Business Bit.
    def post_update_comment_business_bit(self):
        api_url = self.base_url + API.constants.post_update_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'382': 'AS6UOFaf3VUjqP5BgT6eKw==',
                '381': '5DQzfW8UIl63nhd0iBj003/rXbpd4YcM4dcTC/4G2J8='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Update Comment on Requirement or Offering.
    def post_update_comment_requirement_offering(self):
        api_url = self.base_url + API.constants.post_update_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'382': 'NVwDKpQOYm3SkR2iFwb/Wg==',
                '381': '5DQzfW8UIl63nhd0iBj003/rXbpd4YcM4dcTC/4G2J8='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Delete Comment on Business Bit.
    def post_delete_comment_business_bit(self):
        api_url = self.base_url + API.constants.post_delete_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'382': 'AS6UOFaf3VUjqP5BgT6eKw=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Delete Comment on Requirement or Offering.
    def post_delete_comment_requirement_offering(self):
        api_url = self.base_url + API.constants.post_delete_comment
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'382': 'NVwDKpQOYm3SkR2iFwb/Wg=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Get Recommended Posts list.
    def get_recommended_offering_requirement(self):
        api_url = self.base_url + API.constants.get_recommended_posts_v2
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Post from a Network.
    def get_posts_from_a_network(self):
        api_url = self.base_url + API.constants.get_posts_by_network
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '165': 'eJsx+LTCqPGkeptPyywQwA==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '76': 'J1+uTW/L1L+b9YkQgbg2pg==',
                   '153': 'VBVb3ZAFbUMqezuEi8u9qg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get My Post.
    def get_my_posts(self):
        api_url = self.base_url + API.constants.get_my_posts_v3
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '165': 'eJsx+LTCqPGkeptPyywQwA==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '76': 'J1+uTW/L1L+b9YkQgbg2pg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get Notifications.
    def get_notifications(self):
        api_url = self.base_url + API.constants.get_notifications_v2
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '76': 'J1+uTW/L1L+b9YkQgbg2pg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get User Notifications.
    def get_user_notifications(self):
        api_url = self.base_url + API.constants.get_user_notifications_v2
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw==',
                   '76': 'J1+uTW/L1L+b9YkQgbg2pg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Search User.
    def get_search_user(self):
        api_url = self.base_url + API.constants.get_search_user_v2
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '30': 'Iv+wRfeHTFeWcG0ANBfMhA==',
                   '31': 'Iv+wRfeHTFeWcG0ANBfMhA==',
                   '52': 'PFKFobgESplgN6S96CyL2A==',
                   '76': 'J1+uTW/L1L+b9YkQgbg2pg==',
                   '77': 'HfHXvU6ExF63Ky8GwHrepw=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Change Phone number.
    def post_change_phone_no_v3(self):
        api_url = self.base_url + API.constants.post_change_phone_number_v3
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        data = {'7': '8837676566',
                '46': 'OJ1M8Z1pr8Ty0Vf+rSN3sg==',
                '87': 'HjSztcr0nTLBAYz/owx5jw=='}
        response = requests.post(api_url, headers=headers, data=data)
        return response

    # Get networks list by country.
    def get_networks_by_country(self):
        api_url = self.base_url + API.constants.get_networks_by_country
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg==',
                   '360': 'w7GI1ri4hjTc1ZBFhJ7lGA=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get my networks list by country.
    def get_my_networks(self):
        api_url = self.base_url + API.constants.get_my_networks
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        response = requests.get(api_url, headers=headers)
        return response

    # Get countries list.
    def get_countries(self):
        api_url = self.base_url + API.constants.get_countries
        headers = {'50': '1',
                   'Authorization': 'Bearer {0}'.format(authcode),
                   '1': 'cHB/sRc1aMRGSm8aHbRfpg=='}
        response = requests.get(api_url, headers=headers)
        return response
