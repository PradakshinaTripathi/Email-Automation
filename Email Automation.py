import ClointFusion as cf
import cryptocode  

cf.ON_semi_automatic_mode()

name = cf.gui_get_any_input_from_user('Email ID')

password = cf.gui_get_any_input_from_user('Password', True)

toMail = cf.gui_get_any_input_from_user('To')

sub = cf.gui_get_any_input_from_user('Subject')

body = cf.gui_get_any_input_from_user('Enter the Text',multi_line= True)

cf.browser_activate("https://mail.google.com/")
cf.browser_write_h(name,'Email')
cf.browser_mouse_click_h('next')
cf.browser_write_h(password,'Enter the Password')
cf.browser_mouse_click_h('next')
cf.browser_write_h(toMail,"To")
cf.browser_mouse_click_h('Compose')
cf.browser_write_h(sub,'Subject')
cf.browser_mouse_click_h('Next')
cf.key_write_enter(body)
cf.browser_mouse_click_h("send")

cf.browser_wait_until_h("Message sent.Thankyou!")
cf.browser_quit_h()
