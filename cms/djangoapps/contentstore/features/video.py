#pylint: disable=C0111

from lettuce import world, step

############### ACTIONS ####################


@step('when I view the video it does not have autoplay enabled')
def does_not_autoplay(_step):
    assert world.css_find('.video')[0]['data-autoplay'] == 'False'
    assert world.css_find('.video_control')[0].has_class('play')


@step('creating a video takes a single click')
def video_takes_a_single_click(_step):
    assert(not world.is_css_present('.xmodule_VideoModule'))
    world.css_click("a[data-category='video']")
    assert(world.is_css_present('.xmodule_VideoModule'))
