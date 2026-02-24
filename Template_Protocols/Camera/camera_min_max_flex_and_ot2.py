from opentrons.protocol_api import ProtocolContext

metadata = {
    "protocolName": "Camera Test",
    "author": "Opentrons <protocols@opentrons.com>",
}
requirements = {
    "robotType": "Flex",
    "apiLevel": "2.27",
}

def run(protocol: ProtocolContext) -> None:
    protocol.comment('Minimum effort, home after true')
    # protocol.capture_image(home_before=True, filename="within range", zoom=1.0,contrast=0, saturation = 0, brightness = 0)
    protocol.comment('Maximum effort, home after false')
    protocol.capture_image(home_before=True, filename="above max", zoom=2.0, contrast=100 , saturation = 100, brightness = 100)
    protocol.comment('error then comment')
    # protocol.capture_image(home_before=False, filename="below min", zoom=0.9, contrast=0 , saturation = 0, brightness = -1, resolution= (640,480))
    protocol.comment('error then comment zoom')
    protocol.capture_image(home_before=False, filename="below min", zoom=1, contrast=50 , saturation = 50, brightness = 50, resolution= (0,0))
    protocol.comment('Error then comment resolution')
    protocol.capture_image(home_before=True, filename="within range", zoom=1.0, contrast=50, saturation = 50, brightness = 50, resolution =(1000000,1000000))
    protocol.comment('BAD NAMES FOR WINDOWS ')
    Envir_Robot = 'Flex'

    '''
    BAD FILE NAMES 
    '''

    # Test invalid characters
    # The robot (Linux) might allow these, but they will be unusable on Windows.


    ''' 

    protocol.capture_image(home_before=True, filename="image_with_period.", zoom=1.0)
    protocol.comment('Test: Colon :')
    
    protocol.comment('Test: Asterisk *')
    protocol.capture_image(home_before=True, filename="image_with_asterisk_*", zoom=1.0)
    protocol.comment('Test: Colon :')
    protocol.capture_image(home_before=True, filename="image_with_colon:_", zoom=1.0)
    protocol.comment('Test: Question Mark ?')

    protocol.capture_image(home_before=True, filename="image_with_question_mark_?", zoom=1.0)
    protocol.comment('Test: Double Quote "')
    protocol.capture_image(home_before=True, filename="image_with_quotes__", zoom=1.0)
    protocol.comment('Test: Pipe |')

    protocol.capture_image(home_before=True, filename="image_with_pipe_|_", zoom=1.0)
    protocol.comment('Test: Forward Slash /')
    # Slashes will likely be interpreted as directories and fail
    protocol.capture_image(home_before=True, filename="my/folder/image", zoom=1.0)
    protocol.comment('Test: Backslash \\')

    protocol.capture_image(home_before=True, filename="my\\folder\\image", zoom=1.0)
    protocol.comment('Test: Reserved name CON')

    # Test reserved names
    protocol.capture_image(home_before=True, filename="CON", zoom=1.0)
    protocol.comment('Test: Reserved name LPT1')
    
    protocol.capture_image(home_before=True, filename="LPT1", zoom=1.0)
    protocol.comment('Test: Reserved name PRN')

    protocol.capture_image(home_before=True, filename="PRN", zoom=1.0)
    ''' 