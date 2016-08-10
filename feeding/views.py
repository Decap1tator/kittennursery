from django.shortcuts import render
from .models import Litter,Kitten
from django.forms import modelformset_factory


# Create your views here.
def submit_updates(request):
    KittenFormSet = modelformset_factory(Kitten, fields=('pre_feed','post_feed','bathroom'))
    litter = request.POST.get("litter","")

    if request.method == "POST":
        formset = KittenFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            Litter.objects.get(litter=litter).save()

    else:
        return render(request,'feeding/submit_updates_bad.html',{})

    next_feed = Litter.objects.get(litter=litter).next_feed

    return render(request,'feeding/submit_updates.html',{'litter':litter,'next_feed':next_feed})

def update(request):
    update_litter = request.POST.get("litter","")
    KittenFormSet = modelformset_factory(Kitten, fields=('pre_feed','post_feed','bathroom'),extra=0)
    formset = KittenFormSet(queryset=Kitten.objects.filter(litter__litter=update_litter))
    name_to_form = zip(Kitten.objects.filter(litter__litter=update_litter),formset.forms)
    return render(request,'feeding/update.html',{'update_litter':update_litter,'name_to_form':name_to_form,'mgmt':formset.management_form})

def feeding_schedule(request):
    lstatus = Litter.objects.all()
    kstatus = Kitten.objects.all()
    kittensInLitters = {}
    for litter in lstatus:
        kittensInLitters[litter] = []
    for kitten in kstatus:
        p = Litter.objects.filter(litter=kitten.litter)[0]
        kittensInLitters[Litter.objects.filter(litter=kitten.litter)[0]].append(kitten)
    return render(request,'feeding/schedule.html',{'kittensInLitters':kittensInLitters})
