class Params:
    cookies = {
        'guest_id': '173453512022086297',
        'night_mode': '2',
        'guest_id_marketing': 'v1%3A173453512022086297',
        'guest_id_ads': 'v1%3A173453512022086297',
        'gt': '1869401905086017572',
        '_twitter_sess': 'BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74',
        'kdt': 'ngkLSR9ulYSXaDH2GeuoE4Kfoc7D9EXSWsgf6YhY',
        'auth_token': 'b840e6964be1ad7a5761b0cf9bb5bc197be17051',
        'ct0': '46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2',
        'lang': 'en',
        'twid': 'u%3D1869428382863077376',
        'personalization_id': '"v1_1JanKNmWKX7huSYcTzaVCg=="',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json',
        # 'cookie': 'guest_id=173453512022086297; night_mode=2; guest_id_marketing=v1%3A173453512022086297; guest_id_ads=v1%3A173453512022086297; gt=1869401905086017572; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=ngkLSR9ulYSXaDH2GeuoE4Kfoc7D9EXSWsgf6YhY; auth_token=b840e6964be1ad7a5761b0cf9bb5bc197be17051; ct0=46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2; lang=en; twid=u%3D1869428382863077376; personalization_id="v1_1JanKNmWKX7huSYcTzaVCg=="',
        'priority': 'u=1, i',
        'referer': 'https://x.com/albinkurti/status/1868981691580047698',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-client-transaction-id': 'pQy1/RVZRRbKL3rD8g/eDb4VsqVI7f0WCQWmw/FLQdYyv2vAUjdMpCISrg/ZkKeud9Y4tqbPAmxTeOdviOG/W8PVT+77pg',
        'x-csrf-token': '46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
    }

    @staticmethod
    def params_factory(user_id, tweet_id, is_profile=True):
        params_profile = {
            'variables': f'{{"userId":"{user_id}","count":100,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}}',
            'features': '{"profile_label_improvements_pcf_label_in_post_enabled":false,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
            'fieldToggles': '{"withArticlePlainText":false}',
        }

        params_tweet = {
            'variables': f'{{"focalTweetId":"{tweet_id}","with_rux_injections":false,"rankingMode":"Relevance","includePromotedContent":true,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":true,"withBirdwatchNotes":true,"withVoice":true}}',
            'features': '{"profile_label_improvements_pcf_label_in_post_enabled":false,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
            'fieldToggles': '{"withArticleRichContentState":true,"withArticlePlainText":false,"withGrokAnalyze":false,"withDisallowedReplyControls":false}',
        }

        return params_profile if is_profile else params_tweet
