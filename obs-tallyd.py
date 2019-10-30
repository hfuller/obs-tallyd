import obspython as obs

server_host = "127.0.0.1"


### OBS stuff ###

def script_load(settings):
    print("hello")
    script_update(settings)
    set_up_sources()
    tallyd_connect()

def script_unload():
    print("goodbye") #TODO

def script_update(settings):
    global server_host
    server_host = obs.obs_data_get_string(settings, "server")

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "server", "tallyd Server", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, "apply", "Apply", apply_pressed)
    return props


### Setup functions ###

def tallyd_connect():
    tallyd_disconnect()
    print("TODO: tallyd_connect")

def tallyd_disconnect():
    print("TODO: tallyd_disconnect")

def set_up_sources():
    sources = obs.obs_enum_sources()
    for source in sources:
        handler = obs.obs_source_get_signal_handler(source)
        obs.signal_handler_connect(handler, "activate", source_activated)
        obs.obs_source_release(source)
    obs.source_list_release(sources)


### Handlers ###

def source_activated(stuff):
    print("Source activated handler")
    source = obs.calldata_source(stuff, "source")
    print(obs.obs_source_get_name(source))
    #TODO: do stuff
    obs.obs_source_release(source)

def apply_pressed(props, prop):
    tallyd_connect()
