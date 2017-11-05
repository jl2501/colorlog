import logging
import kaleidoscope
from collections import UserDict

def get_default_colormap():
    return(
        {
            'DEBUG'     : [ kaleidoscope.Color('bright lightcyan on lightblack'),
                            kaleidoscope.Color('bright lightcyan on black')],

            'INFO'      : [ kaleidoscope.Color('bright black on lightblack'),
                            kaleidoscope.Color('bright lightblack on black')],

            'WARNING'   : [ kaleidoscope.Color('bright black on lightyellow'),
                            kaleidoscope.Color('bright lightyellow on black')],

            'ERROR'     : [ kaleidoscope.Color('bright lightred on lightwhite'),
                            kaleidoscope.Color('bright lightred on black')],

            'CRITICAL'  : [ kaleidoscope.Color('bright lightwhite on lightred'),
                            kaleidoscope.Color('bright lightred on black')]
        }
    )


class ColorFormatter(logging.Formatter):
    ''' 
    Description:
        Python Logging facility Formatter subclass that uses the LogColorMapping to create
        a formatted log message with the level in the first color and the rest of the
        message in the second color.

    Notes:
        To extend this, add needed attributes to the LogRecord in format(), but
        reference those attributes in the format string in __init__
    '''
    def __init__(self, colormap=None, fmt=None, datefmt=None, style='%'):
        ''' 
        Input:
            colormap: nested dict with the following structure:
                outer key: string version of logging levels:  
                    (DEBUG, INFO, WARNING, ERROR, CRITICAL)

                inner key: one of "level_color" or "message_color", used to color the
                    level and the message output
                
            fmt, datefmt, style: passed to super().__init__() as is.
        '''
        if fmt is None:
            fmt = ("%(color0)s%(levelname)s:%(color_reset)s" +
                   "%(color1)s %(name)s: %(message)s %(color_reset)s")
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

        if colormap is None:
            self.colormap = get_default_colormap()
        else:
            self.colormap = colormap


    def format(self, record):
        strlevel = logging.getLevelName(record.levelno)
        record.color_reset = kaleidoscope.Color.terminal_reset()
        #- set color0..colorN attributes to be the terminal codes
        for n, color_x in enumerate(self.colormap[strlevel]):
            terminal_codes = self.colormap[strlevel][n].terminal_codes()
            setattr(record, 'color{}'.format(str(n)), terminal_codes)
        record.colors = self.colormap[strlevel]
        s = super().format(record)
        return s

