from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Litter(models.Model):
    ROOM_NAMES = (
        ('A','Room A'),
        ('B','Room B'),
        ('C','Room C'),
        ('D','Room D'),
    )
    FOOD_TYPES = (
        (2,'Gruel'),
        (3,'Wet'),
        (5,'Dry'),
        (4,'Wet/Dry'),
    )
    litter = models.CharField(max_length=4,unique=True)
    room = models.CharField(max_length=6,choices=ROOM_NAMES)
    arrival = models.DateTimeField()
    foodtype = models.IntegerField(choices=FOOD_TYPES)
    last_feed = models.DateTimeField(blank=True)
    next_feed = models.DateTimeField(editable=False)
    def gratudate(self):
        #move litter out of nursery
        pass

    def feed(self,when):
        last_feed = when

    def __str__(self):
        return(self.litter)

    def save(self):
        #self.foodtype = foodtype
        self.last_feed = datetime.datetime.now()
        if self.foodtype == 2:
            self.next_feed = self.last_feed+datetime.timedelta(0,7200)
        elif self.foodtype == 3:
            self.next_feed = self.last_feed+datetime.timedelta(0,10800)
        elif self.foodtype == 4:
            self.next_feed = self.last_feed+datetime.timedelta(0,14400)
        elif self.foodtype == 5:
            self.next_feed = self.last_feed+datetime.timedelta(0,18000)
        super(Litter,self).save()

class Kitten(models.Model):
    BATHROOM_TYPES = (
        ('urine','urine'),
        ('bm','bowel movement'),
        ('none','none'),
    )
    litter = models.ForeignKey(Litter)
    name = models.CharField(max_length=24)
    pre_feed = models.IntegerField(db_column='lastWeight')
    wtDelta = models.IntegerField(blank=True,null=True)
    post_feed = models.IntegerField(blank=True,null=False)
    bathroom = models.CharField(max_length=12, choices=BATHROOM_TYPES,blank=True,null=False)

    def __str__(self):
        return(self.name)

    def safe(self,pre_feed,new_weight):
        #have parents model call this to update each kitten
        self.pre_feed = pre_feed
        self.post_feed = new_weight
        self.wtDelta = self.pre_feed - self.post_feed
        super(Kitten,self).save()

