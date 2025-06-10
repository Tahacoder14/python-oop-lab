"""
Task 15: Polymorphism (Duck Typing) - If It Quacks Like a Duck...
Concept:
Polymorphism ("many forms") in Python often uses "duck typing":
An object's suitability for an operation is determined by whether it has the
required methods/attributes, NOT by its explicit type.
If it walks like a duck and quacks like a duck, it's treated as a duck.
Let's make different 'Communicator' objects send messages.
"""

class EmailSender:
    def __init__(self, sender_address):
        self.sender_address = sender_address
        print(f"EmailSender configured for {self.sender_address}")

    def send_message(self, recipient, message_text): # Method name is key
        print(f"EMAIL from {self.sender_address} to {recipient}:")
        print(f"  Subject: Important Update")
        print(f"  Body: {message_text}")
        print(f"--- Email Sent ---")

class SMSSender:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        print(f"SMSSender configured for {self.phone_number}")

    def send_message(self, recipient_phone, message_text): # Same method name
        print(f"SMS from {self.phone_number} to {recipient_phone}:")
        print(f"  '{message_text}'")
        print(f"--- SMS Sent ---")

class CarrierPigeon:
    def __init__(self, pigeon_name, home_coop_location):
        self.pigeon_name = pigeon_name
        self.home_coop = home_coop_location
        print(f"CarrierPigeon '{self.pigeon_name}' ready at {self.home_coop}.")

    # CarrierPigeon also has a 'send_message' method, but with different params
    # For a stricter polymorphism, it should match the most common signature,
    # or the dispatcher function needs to be smarter.
    # Here, we'll adapt our dispatcher.
    def send_message(self, destination_coop, scroll_content):
        print(f"PIGEON POST by '{self.pigeon_name}' from {self.home_coop} to {destination_coop}:")
        print(f"  Scroll Message: '{scroll_content}'")
        print(f"--- Pigeon Dispatched ---")

class FaxMachine: # Does NOT have 'send_message'
    def __init__(self, fax_number):
        self.fax_number = fax_number
        print(f"FaxMachine {self.fax_number} online.")

    def transmit_document(self, recipient_fax, document_path):
        print(f"FAX from {self.fax_number} to {recipient_fax}:")
        print(f"  Transmitting document: {document_path}")
        print(f"--- Fax Transmitted ---")


# This function demonstrates polymorphism. It works with any object
# that has a 'send_message' method, adapting to its signature.
def dispatch_communication(communicator_obj, recipient, message, alt_recipient=None, alt_message=None):
    print(f"\nAttempting to send via {type(communicator_obj).__name__}:")
    try:
        if isinstance(communicator_obj, CarrierPigeon):
            # CarrierPigeon has a different signature
            communicator_obj.send_message(alt_recipient or "Default Coop", alt_message or message)
        elif hasattr(communicator_obj, 'send_message'): # Check if method exists
            communicator_obj.send_message(recipient, message)
        else:
            print(f"Object {communicator_obj} does not have a 'send_message' method.")
            if hasattr(communicator_obj, 'transmit_document'): # Check for alternative
                print("But it can 'transmit_document'. Trying that...")
                communicator_obj.transmit_document(recipient, f"Document: {message}")

    except AttributeError as e:
        print(f"  Error: Could not use 'send_message' on {type(communicator_obj).__name__}. {e}")
    except TypeError as e: # For mismatched arguments if not handled above
        print(f"  Error: Argument mismatch for 'send_message' on {type(communicator_obj).__name__}. {e}")

def get_input_params():
    return [
        {"name": "email_sender_addr", "label": "Email Sender Address:", "type": "text_input", "default": "me@example.com"},
        {"name": "sms_sender_phone", "label": "SMS Sender Phone:", "type": "text_input", "default": "+15551234567"},
        {"name": "pigeon_name_val", "label": "Pigeon's Name:", "type": "text_input", "default": "Archimedes"},
        {"name": "recipient_email", "label": "Recipient Email/Fax:", "type": "text_input", "default": "you@example.com"},
        {"name": "recipient_phone", "label": "Recipient Phone:", "type": "text_input", "default": "+15557654321"},
        {"name": "pigeon_dest_coop", "label": "Pigeon Destination Coop:", "type": "text_input", "default": "North Tower"},
        {"name": "message_content", "label": "Message Content:", "type": "text_input", "default": "Hello from the OOP Lab!"}
    ]

def run_task(email_sender_addr, sms_sender_phone, pigeon_name_val, recipient_email, recipient_phone, pigeon_dest_coop, message_content):
    emailer = EmailSender(email_sender_addr)
    texter = SMSSender(sms_sender_phone)
    pigeon = CarrierPigeon(pigeon_name_val, "My Balcony")
    fax = FaxMachine("555-0199")

    communicators = [emailer, texter, pigeon, fax]

    print("\n--- Sending messages using different communicators (Polymorphism) ---")
    for comm_device in communicators:
        # Adapt recipient/message based on device for demo
        current_recipient = recipient_email
        if isinstance(comm_device, SMSSender):
            current_recipient = recipient_phone
        elif isinstance(comm_device, CarrierPigeon):
            # For CarrierPigeon, dispatch_communication handles alt_recipient/alt_message
            dispatch_communication(comm_device, recipient_email, message_content,
                                   alt_recipient=pigeon_dest_coop, alt_message=f"Secret plans: {message_content[:10]}...")
            continue # Skip default dispatch for pigeon as it's handled

        dispatch_communication(comm_device, current_recipient, message_content)

    print("\nPolymorphism allows treating objects of different classes in a uniform way,")
    print("as long as they support the expected 'interface' (e.g., a 'send_message' method).")

if __name__ == "__main__":
    run_task("sender@lab.com", "+1000111222", "Hedwig", "receiver@lab.com", "+1999888777", "Distant Castle", "The eagle has landed.")