class Solution:
    def numUniqueEmails(self, emails):
        final_list = []
        for email in emails:
            end = email.index("@")
            if "." in email[:end]:
                email = email[:end].replace(".","")+email[end:]
            if "+" in email:
                start = email.index("+")
                endagain = email.index("@")
                email = email[:start]+email[endagain:]
            else:
                final_list.append(email)
            final_list.append(email)

        final = len(set(final_list))
        return final

s = Solution()
emails = ["j+ezsorqlmc@rfpycgjuf.com","j+k+ri+rigt.ad@rfpycgjuf.com","hfmeqzk.isx+i@fiidmdrsu.com","j+p+h+d+d+p+z.j.k.g@rfpycgjuf.com","zygekdy.l.w+s@snh.owpyu.com","j+m.l+ia+qdgv+w@rfpycgjuf.com","r+hwbjwefkp@wcjaki.n.com","zygekdy.l.w+d@snh.owpyu.com","bizdm+sz.f.a.k@il.cjjlp.com","hfmeqzk.isx+t@fiidmdrsu.com","hfmeqzk.isx+i@fiidmdrsu.com","bizdm+f+j+m.l.l@il.cjjlp.com","zygekdy.l.w+g@snh.owpyu.com","r+evgvxmksf@wcjaki.n.com","hfmeqzk.isx+h@fiidmdrsu.com","bizdm+lov+cy@il.cjjlp.com","hfmeqzk.isx+o@fiidmdrsu.com","bizdm+hs+qao@il.cjjlp.com","r+v+z+rcuznrj@wcjaki.n.com","j+r.kn+h.w.a.h+bh@rfpycgjuf.com","hfmeqzk.isx+t@fiidmdrsu.com","hfmeqzk.isx+a@fiidmdrsu.com","zygekdy.l.w+o@snh.owpyu.com","zygekdy.l.w+i@snh.owpyu.com","r+vy.u.y+f.er+aw@wcjaki.n.com","zygekdy.l.w+c@snh.owpyu.com","bizdm+wztzg@il.cjjlp.com","j+h.fwbsr+chp@rfpycgjuf.com","zygekdy.l.w+s@snh.owpyu.com","zygekdy.l.w+d@snh.owpyu.com","bizdm+qq.o.q+p@il.cjjlp.com","zygekdy.l.w+o@snh.owpyu.com","j+c+zqbq+h.dyt@rfpycgjuf.com","r+hl.b.i+fz.hz.t@wcjaki.n.com","r+cbabpf.k+w+e@wcjaki.n.com"]

print(s.numUniqueEmails(emails))
