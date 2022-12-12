from django.shortcuts import render
from screens.models import Weight_distribution
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.template import loader
from Authentication.decorators import unauthenticated_user, allowed_users

def introduction(request):
    return render(request, 'introduction.html')
    
def first_screen(request):
        from screens.models import Customer_Type, Juridictional_Risk, List_Matching, Profile_linkage, Product_Service, \
            Transaction_Behavior
        context = {
            'cty': Customer_Type.objects.all(),
            'pds': Product_Service.objects.all(),
            'jdr': Juridictional_Risk.objects.all(),
            'ltm': List_Matching.objects.all(),
            'pfl': Profile_linkage.objects.all(),
            'tsb': Transaction_Behavior.objects.all(),      
        }
        return render(request, 'first-screen.html', context)

@allowed_users(allowed_roles=['Admin'])
def weight_distribution(request):
    context = {
        'wtd': Weight_distribution.objects.all()
    }
    return render(request, 'weight_distribution.html', context)

@allowed_users(allowed_roles=['Admin'])
def weight_distribution_edit(request):
    from screens.models import Weight_distribution
    context = {
        'wtd1': Weight_distribution.objects.all()
            }
    if request.method == 'POST':
        if request.POST.get("Weight"):
         post=Weight_distribution()
         post.Weight= request.POST.get('Weight')
         post.save()
        return render(request, 'weight_distribution_edit.html',context)
    else:
        return render(request, 'weight_distribution_edit.html',context)

def score(request):
    from screens.models import Customer_Type, Weight_distribution, Juridictional_Risk, List_Matching, Profile_linkage, \
        Product_Service, \
        Transaction_Behavior
    if request.method == 'POST':
        ct = request.POST.get('Customer_Types')
        ps = request.POST.get('product_service')
        cj = request.POST.get('cj')
        lm = request.POST.get('list_matching')
        pl = request.POST.get('profile_linkage')
        tb = request.POST.get('tb')
        ## To fetch all the values from database
        cty = pd.DataFrame(list(Customer_Type.objects.all().values()))
        pds = pd.DataFrame(list(Product_Service.objects.all().values()))
        jdr = pd.DataFrame(list(Juridictional_Risk.objects.all().values()))
        ltm = pd.DataFrame(list(List_Matching.objects.all().values()))
        pfl = pd.DataFrame(list(Profile_linkage.objects.all().values()))
        tsb = pd.DataFrame(list(Transaction_Behavior.objects.all().values()))
        wtd = pd.DataFrame(list(Weight_distribution.objects.all().values()))
 
        
    
        customer_types = []
        ct_score = []
        ct=[]
        a = len(cty)
        for i in range(a):
            # print(request.POST.get(str(i)))
            if request.POST.get('ct' + str(i + 1)):
                customer_types.append(i + 1)
        # ct_score= [cty['Score'] for i in cty: cty['id'] in customer_types]
        for index, row in cty.iterrows():
            if row['id'] in customer_types:
                ct_score.append(row['Score'])
        for index, row in cty.iterrows():
            if row['id'] in customer_types:
                ct.append(row['Customer_Category'])
              
        for i in range(len(ct)):
           ct1="\n".join("{} {}".format(x, y) for x, y in zip(ct, ct_score))
        final_ct_score = max(ct_score)

        request.session['ct']=ct

        product_service = []
        ps_score = []
        ps=[]
        a = len(pds)
        for i in range(a):
            if request.POST.get('ps' + str(i + 1)):
                product_service.append(i + 1)
        for index, row in pds.iterrows():
            if row['id'] in product_service:
                ps_score.append(row['Score'])
        for index, row in pds.iterrows():
            if row['id'] in product_service:
                ps.append(row['Product'])
        for i in range(len(ps)):
           ps1="\n".join("{} {}".format(x, y) for x, y in zip(ps, ps_score))
        final_ps_score = max(ps_score)
        request.session['ps']=ps

        jdr_score = []
        js=[]
        for index, row in jdr.iterrows():
            if row['Country_Juridiction'] in cj:
                jdr_score.append(row['Score'])
        for index, row in jdr.iterrows():
            if row['Country_Juridiction'] in cj:
                js.append(row['Country_Juridiction'])
       
        jdr1 = jdr_score[0]
        for i in range(len(js)):
           js1="\n".join("{} {}".format(x, y) for x, y in zip(js, jdr_score))
        request.session['js']=js
   
        # for i in jdr_score:
        #     print(i, end="")
    

        # Country_Juridiction = []
        # for i in range(74):
        #     if request.POST.get('cj'+str(i)):
        #         Country_Juridiction.append('cj'+str(i))

        # list_matching = []
        # lm_score=[]
        # a = len(ltm)
        # for i in range(a):
        #     if request.POST.get('lm' + str(i+1)):
        #         list_matching.append(i+1)

        # for index, row in ltm.iterrows():
        #     if row['id'] in list_matching:
        #         lm_score.append(row['Score'])
        # print(lm_score)

        profile_linkage = []
        pl_score = []
        pl=[]
        a = len(pfl)
        
        for i in range(a):
            if request.POST.get('pl' + str(i + 1)):
                profile_linkage.append(i + 1)
                
        for index, row in pfl.iterrows():
            if row['id'] in profile_linkage:
                pl_score.append(row['Score'])
        for index, row in pfl.iterrows():
            if row['id'] in profile_linkage:
                pl.append(row['Parameters'])
        pl1=[]
        pl1.append(pl_score)
        for i in range(len(pl)):
           pl1="\n".join("{} {}".format(x, y) for x, y in zip(pl, pl1))
        final_pl_score = max(pl_score,default=0)
        # print(pl1)
        request.session['pl']=pl
        
        Transaction_Behavior = []
        a = len(tsb)
        for i in range((a) + 1):
            if request.POST.get('tb' + str(i)):
                Transaction_Behavior.append(request.POST.get('tb' + str(i)))
        
        score_tsb = 0
        tsb_score = []
        tsb1=[]
        for i in range(len(tsb)):
            freq = request.POST.get('tb' + str(i + 1))
            #print("freq"+freq)
            if freq == '1':
                score_tsb = tsb['Score_one'][i]
                # print(score_tsb)
                tsb_score.append(score_tsb)

            if freq == '2':
                score_tsb = tsb['Score_two'][i]
                # print(score_tsb)
                tsb_score.append(score_tsb)

            if freq == '3':
                score_tsb = tsb['Score_three'][i]
                # print(score_tsb)
                tsb_score.append(score_tsb)
                

            else:
                pass

        final_tsb_score = max(tsb_score,default=0)
       

        list_matching = []

        a = len(ltm)

        for i in range(a + 1):

            if request.POST.get('lm' + str(i)):
                list_matching.append(request.POST.get('lm' + str(i)))

        # print(list_matching)
        lm = []
        lm1=[]
        for i in list_matching:
            if i != 'None':
                lm.append(i)

       
        
        lm = [eval(i) for i in lm]
        lm = max(lm,default=0)

        p = wtd['Weight'].tolist()

        final_score = [lm, final_tsb_score, final_ct_score, final_ps_score]
        final_score.extend(jdr_score)
        final_score.append(final_pl_score)
       
        max_final_score=final_score.index(max(final_score))
        min_final_score=final_score.index(min(final_score))
       
        final_score1 = 0
        for i in range(0, len(p)):
            final_score1 = final_score1 + (p[i] * final_score[i])

        final_score1 = final_score1 / 100
        # print(jdr1)
        context = {
            'Customer_Types': customer_types,
            'product_service': product_service,
            'country_jurisdiction': cj,
            # 'list_matching': list_matching,
            'profile_linkage': profile_linkage,
            'tb': Transaction_Behavior,
            'final_ct_score': final_ct_score,
            'final_ps_score': final_ps_score,
            'final_pl_score': final_pl_score,
            'final_tsb_score': final_tsb_score,
            'ct_score': ct_score,
            'pl_score': pl_score,
            'ps_score': ps_score,
            'tsb_score': tsb_score,
            'jdr_score': jdr_score,
            'total': final_score1,
            'lm': lm,
            'jdr1': jdr1,
            'max_final_score':max_final_score,
            'min_final_score':min_final_score,
            'ps1':ps1,
            'js1':js1,
            'pl1':pl1,
            'ct1':ct1,
            'lm1':lm1,
            'jdr1':jdr1
        }
        return render(request, 'score.html', context)
    return render(request, 'score.html')



