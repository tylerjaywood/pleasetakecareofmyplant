import gsrpeadsheet_tool as gs
import config as c

r = c.getReddit()

# Checks if there are any people that want to unsubscribe and remove them
# from the list
def check_for_unsubscribes(wks):
    # Get unread inbox messages
    g = r.get_unread()
    for message in g:
        # If someone wants to unsubscribe
        if message.body == "!unsubscribe":
            # delete them from the list
            gs.unsub(wks, str(message.author.name))
            # and check the unsubscribe message as read
            message.mark_as_read()


# Send message to everyone in the mailing list
def broadcast(subject, message):
    # Get the worksheet
    wks = gs.get_worksheet(c.mailing_list_id)
    # Check if there are any people that want to unsubscribe
    check_for_unsubscribes(wks)
    # Get the mailing list
    users = gs.get_list(wks)
    for user in users:
        # Send message for each user in the mailing list
        r.send_message(user, subject, message)
