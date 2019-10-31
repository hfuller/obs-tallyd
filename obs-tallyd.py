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
        obs.signal_handler_connect(handler, "deactivate", source_deactivated)
        obs.signal_handler_connect(handler, "hide", source_hidden)
        obs.signal_handler_connect(handler, "show", source_shown)
        #obs.obs_source_release(source)
    obs.source_list_release(sources)


### Handlers ###

def source_tally_changed(handler_name, stuff):
    """Function that only exists to centralize the handler logic."""

    print("Source handler:", handler_name)

    source = obs.calldata_source(stuff, "source")
    print(obs.obs_source_get_name(source))

    if handler_name == "activate":
        print("TODO: set live tally")
    elif handler_name == "deactivate":
        if obs.obs_source_showing(source):
            print("TODO: set preview tally")
        else:
            print("TODO: clear tally")
    elif handler_name == "show":
        if obs.obs_source_active(source): #should never happen unless handlers fire in a weird order
            print("TODO: set live tally")
        else:
            print("TODO: set preview tally")
    elif handler_name == "hide":
        print("TODO: clear tally")
    else:
        print("I don't know what kind of handler is", handler_name)

    #obs.obs_source_release(source)

def source_activated(stuff):
    source_tally_changed("activate", stuff)
def source_deactivated(stuff):
    source_tally_changed("deactivate", stuff)
def source_hidden(stuff):
    source_tally_changed("hide", stuff)
def source_shown(stuff):
    source_tally_changed("show", stuff)

def apply_pressed(props, prop):
    tallyd_connect()
