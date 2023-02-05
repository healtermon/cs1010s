def make_image(height, width):
    return (height, width)

def height(img):
    return img[0]

def width(img):
    return img[1]
    
def make_lens(name, a, b, c, d):
    return (name, a, b, c, d)

def name(lens):
    return lens[0]

def beam(lens, img):
    h = height(img)
    w = width(img)
    a = lens[1]
    b = lens[2]
    c = lens[3]
    d = lens[4]
    return make_image((h*a)+(w*c),(h*b)+(w*d))

def make_projector(name):
    return (name,)

def place_lens(proj, lens):
    return proj + (lens,)

def get_lenses(proj):
    return tuple(map(lambda lens: name(lens),proj[1:]))

def projection(proj,img):
    for lens in proj[1:]:
        img = beam(lens,img)
    return img

# New version

def make_projector(name):
    return ("#projector",name,)

def is_projector(proj):
    return type(proj)==tuple and len(proj)>1 and proj[0]=="#projector"

def place_lens(proj, lens):
    if is_projector(lens):
        return proj + lens[2:]
    else:
        return proj + (lens,)

def get_lenses(proj):
    return tuple(map(lambda lens: name(lens),proj[2:]))

def projection(proj,img):
    for lens in proj[2:]:
        img = beam(lens,img)
    return img

cinema = make_projector("Cinema") # make a cinematic projector
upside_down = make_lens("UpsideDown", -1, 0, 0, 1)
enlarge_double = make_lens("Enlarge2X", 2, 0, 0, 2)
widen = make_lens("Widen", 1, 0, 0, 4)
cinema = place_lens(cinema, enlarge_double)
cinema = place_lens(cinema, upside_down)
cinema = place_lens(cinema, enlarge_double)
cinema = place_lens(cinema, widen) # made for widescreen
print(projection(cinema,make_image(10,10)))
vintage_proj = cinema
cinema = place_lens(cinema, vintage_proj)
print(projection(cinema,make_image(10,10)))

class Image:

    def __init__(self,height, width):
        self.height = height
        self.width = width
        
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
    
    def __str__(self):
        return "("+str(self.height)+","+str(self.width)+")"
    
class Lens:
    
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def name(self):
        return self.name

    def beam(self, img):
        h = img.get_height()
        w = img.get_width()
        return Image((h*self.a)+(w*self.c),(h*self.b)+(w*self.d))

class Projector:
    
    def __init__(self,name):
        self.name = name
        self.lenses = []
        
    def place_lens(self, lens):
        if type(lens)==Projector:
            self.lenses.extend(lens.lenses)
        else:
            self.lenses.append(lens)

    def get_lenses(self):
        return tuple(map(lambda lens: lens.name(),self.lenses))
    
    def projection(self,img):
        for lens in self.lenses:
            img = lens.beam(img)
        return img


cinema = Projector("Cinema") # make a cinematic projector
upside_down = Lens("UpsideDown", -1, 0, 0, 1)
enlarge_double = Lens("Enlarge2X", 2, 0, 0, 2)
widen = Lens("Widen", 1, 0, 0, 4)
cinema.place_lens(enlarge_double)
cinema.place_lens(upside_down)
cinema.place_lens(enlarge_double)
cinema.place_lens(widen) # made for widescreen
print(cinema.projection(Image(10,10)))
vintage_proj = cinema
cinema.place_lens(cinema)
print(cinema.projection(Image(10,10)))

# Newer version
class Image:

    def __init__(self,height, width):
        self.height = height
        self.width = width
        
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
    
    def __str__(self):
        return "("+str(self.height)+","+str(self.width)+")"
    
class Lens:
    
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_name(self):
        return self.name

    def beam(self, img):
        h = img.get_height()
        w = img.get_width()
        return Image((h*self.a)+(w*self.c),(h*self.b)+(w*self.d))

class Projector:
    
    def __init__(self,name):
        self.name = name
        self.lenses = []
        
    def place_lens(self, lens):
        self.lenses.append(lens)

    def get_lenses(self):
        result = []
        for lens in self.lenses:
            if type(lens)==Projector:
                result.extend(lens.get_lenses())
            else:
                result.append(lens.get_name())            
        return result
    
    def projection(self,img):
        for lens in self.lenses:
            if type(lens)==Projector:
                img = lens.projection(img)
            else:
                img = lens.beam(img)
        return img

    def pop(self):
        if self.lenses:
            self.lenses.pop()


cinema = Projector("Cinema") # make a cinematic projector
upside_down = Lens("UpsideDown", -1, 0, 0, 1)
enlarge_double = Lens("Enlarge2X", 2, 0, 0, 2)
widen = Lens("Widen", 1, 0, 0, 4)
cinema.place_lens(enlarge_double)
cinema.place_lens(upside_down)
cinema.place_lens(enlarge_double)
cinema.place_lens(widen) # made for widescreen
print(cinema.projection(Image(10,10)))
vintage_proj = Projector("Vintage")
vintage_proj.place_lens(enlarge_double)
vintage_proj.place_lens(upside_down)
vintage_proj.place_lens(enlarge_double)
vintage_proj.place_lens(widen) # made for widescreen
cinema.place_lens(vintage_proj)
print(cinema.projection(Image(10,10)))




