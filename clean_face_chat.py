def clean_face_chat(data):

    import emoji

    corpus = []
    conversacion = []
    i = 0
    for message in sorted(data['messages'], key= lambda x: x['timestamp_ms']):
        if 'content' in message and not [x for x in ['de amistad en Facebook','Messenger','https','archivo adjunto','al grupo el nombre','foto del grupo.'] if x in message['content']] and not emoji.get_emoji_regexp().search(message['content'].encode('latin1').decode('utf8')):
            #print(f"{message['content'].encode('latin1').decode('utf8')},{message['sender_name']}\n")
            if i == 0:
                conversacion.append({
                    "mensaje":message['content'],
                    "persona":message['sender_name']
                })
                i = 1

            elif i == 1:
                if conversacion[0]['persona'] == message['sender_name']:
                    conversacion[0]['mensaje'] = f"{conversacion[0]['mensaje']}. {message['content']}"
                else:
                    conversacion.append({
                        "mensaje":message['content'],
                        "persona":message['sender_name']
                    })
                    i = 2

            elif i == 2:
                if conversacion[1]['persona'] == message['sender_name']:
                    conversacion[1]['mensaje'] = f"{conversacion[1]['mensaje']}. {message['content']}"
                else:
                    corpus.append(conversacion)
                    conversacion = []
                    i = 0

    list = []
    for part in corpus:
        list.append([part[0]['mensaje'].encode('latin1').decode('utf8'),part[1]['mensaje'].encode('latin1').decode('utf8')])
    return list
