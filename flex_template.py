def flex_template(df):
    global msg
    content = []
    for i in range(5):
        content.append({
            "type": "bubble",
            "size": "mega",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": df.values[i][1],
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "公司名稱 :",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": df.values[i][2],
                                        # "wrap": true,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 3
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "公司地點 :",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": df.values[i][3],
                                        # "wrap": true,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 3
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "薪資 :",
                                        "flex": 1,
                                        "size": "sm",
                                        "color": "#aaaaaa"
                                    },
                                    {
                                        "type": "text",
                                        "text": df.values[i][5],
                                        "color": "#666666",
                                        "flex": 3,
                                        "size": "sm"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "WEBSITE",
                            "uri": df.values[i][6]
                        }
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                ],
                "flex": 0
            },
            "action": {
                "type": "uri",
                "label": "action",
                "uri": df.values[i][6]
            }
        })

    msg = {"type": "carousel", "contents": content}

    return msg
