from watson_developer_cloud import AssistantV1
import excel_reader
import json
from models.collection import Message
import mlab
mlab.connect()

assistant = AssistantV1(
    version = "2018-08-01",
    username = "04771e9c-688f-402f-852e-55e1874b5b54",
    password = "dLH1BuPMf5N7",
    url = "https://gateway.watsonplatform.net/assistant/api"
)

def json_decode_utf8(response):
    json_string = json.dumps(response, indent = 2, ensure_ascii=False)
    json_string.encode("utf-8")
    return json_string
def save_data(role,message):
    new_message = Message(role= role,message=message)
    new_message.save()

workspace_id = "dff6b370-5125-47ca-8dcc-6b5b0332e605"

def bot_response(user_input):
    user_input = user_input
    save_data(role="user",message=user_input)

    context_preresponse = None


    response = assistant.message(
        workspace_id = workspace_id,
        context = context_preresponse,
        input = {
            "text":user_input
        }
    ).get_result()

    # context use to continue the text of a conversation
    context_preresponse = response["context"]
    if response['intents']:
        #check ngày/thang
        if response['intents'][0]['intent'] == 'xem_mã_VN_Index':
            # print(response)
            # print(response['intents'][0]['intent'])
            info_dict = excel_reader.get_info(entities_list = response['entities'])
            if(info_dict is not None):
                print("thông tin mã {0} ngày {1} tháng {2} :".format(response['entities'][0]['value'],response['entities'][1]['value'],response['entities'][2]['value']))
                print("Open: {0} \nHigh: {1} \nLow: {2} \nClose: {3} \nVolume: {4}".format(info_dict["Open"],info_dict["High"],info_dict["Low"],info_dict["Close"],info_dict["Volume"]))
                save_data(role="bot",message='thông tin mã {0} ngày {1} tháng {2} :'.format(response['entities'][0]['value'],response['entities'][1]['value'],response['entities'][2]['value']))
                save_data(role="bot",message='Open: {0} \nHigh: {1} \nLow: {2} \nClose: {3} \nVolume: {4}'.format(info_dict["Open"],info_dict["High"],info_dict["Low"],info_dict["Close"],info_dict["Volume"]))
            else:
                print("dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")
                save_data(role="bot",message="dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")
        #check ngay/thang/giờ
        if response["intents"][0]["intent"] == "xem_mã_ngày_tháng_giờ":
            # print(response)
            info_dict = excel_reader.get_info(entities_list=response['entities'])
            if(info_dict is not None):
                print("thông tin mã {0} ngày {1} tháng {2}lúc{3} giờ :".format(response['entities'][0]['value'],response['entities'][2]['value'],response['entities'][3]['value'],response['entities'][1]['value']))
                print("Open: {0} \nHigh: {1} \nLow: {2} \nClose: {3} \nVolume: {4}".format(info_dict["Open"],info_dict["High"],info_dict["Low"],info_dict["Close"],info_dict["Volume"]))
                save_data(role="bot",message="thông tin mã {0} ngày {1} tháng {2}lúc{3} giờ :".format(response['entities'][0]['value'],response['entities'][2]['value'],response['entities'][3]['value'],response['entities'][1]['value']))
                save_data(role="bot",message="Open: {0} \nHigh: {1} \nLow: {2} \nClose: {3} \nVolume: {4}".format(info_dict["Open"],info_dict["High"],info_dict["Low"],info_dict["Close"],info_dict["Volume"]))
            else:
                print("dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")
                save_data(role="bot",message="dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")
        #check ngày/thang/giờ-giờ
        if response["intents"][0]["intent"] == "xem_mã_ngày_tháng_từ_giờ_đến_giờ":
            # print(response)
            info_dict = excel_reader.get_info(entities_list=response['entities'])
            if(info_dict is not None):
                print("thông tin mã {0} ngày {1} tháng {2} từ {3} giờ đến {4} giờ :".format(response['entities'][0]['value'],response['entities'][1]['value'],response['entities'][2]['value'],response['entities'][3]['value'],response['entities'][4]['value']))
                save_data(role="bot",message="thông tin mã {0} ngày {1} tháng {2} từ {3} giờ đến {4} giờ :".format(response['entities'][0]['value'],response['entities'][1]['value'],response['entities'][2]['value'],response['entities'][3]['value'],response['entities'][4]['value']))
                for info in info_dict:
                    print(info)
                    print("Time: {0}h{1}' \nOpen: {2} \nHigh: {3} \nLow: {4} \nClose: {5} \nVolume: {6}".format(info['Hour'],info['Minute'],info["Open"],info["High"],info["Low"],info["Close"],info["Volume"]))
                    save_data(role="bot",message="Time: {0}h{1}' \nOpen: {2} \nHigh: {3} \nLow: {4} \nClose: {5} \nVolume: {6}".format(info['Hour'],info['Minute'],info["Open"],info["High"],info["Low"],info["Close"],info["Volume"]))
            else:
                print("dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")
                save_data(role="bot",message="dữ liệu không tồn tại, bạn vui lòng xem ngày hôm khác")

    if response['output']['generic']:
        #--print text--
        # print(response['output']['generic'][0]['text'])
        #--print response_type--
        # print(response["output"]["generic"][0]["response_type"])
        #--print title --
        # print(response['output']['generic'][0]["title"])
        #--print intent--
        # print(response['intents'][0]['intent'])
        #--print context--
        #print(response['context'])
        if response["output"]["generic"][0]["response_type"] == "text":
            print(response)
            print(response['output']['generic'][0]['text'])
            save_data(role="bot",message=response['output']['generic'][0]['text'])
        if response["output"]["generic"][0]["response_type"] == "image":
            print(response['output']['generic'][0]['title'])
            print(response['output']['generic'][0]['source'])
            save_data(role="bot",message=response['output']['generic'][0]['title'])
            save_data(role="bot",message=response['output']['generic'][0]['source'])
        if response["output"]["generic"][0]["response_type"] == "option":
            print(response['output']['generic'][0]["title"])
            save_data(role="bot",message=response['output']['generic'][0]["title"])
            options = response['output']['generic'][0]['options']
            for i in range (len(options)):
                print(response['output']['generic'][0]['options'][i]["label"])
                save_data(role="bot",message=response['output']['generic'][0]['options'][i]["label"])
