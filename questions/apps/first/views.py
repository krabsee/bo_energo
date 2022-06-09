from django.shortcuts import render
from django.views.generic import TemplateView
import random
from .forms import ColorForm, CalculatorForm


class Index(TemplateView):
    template_name = 'index.html'


class QuadraticEquation(TemplateView):
    template_name = 'quadratic_equation.html'

    def get(self, request, **kwargs):
        first_coefficient = ''
        second_coefficient = ''
        third_coefficient = ''
        form = CalculatorForm(request.POST or None)
        if form.is_valid():
            print('FORM IS VALID')
        context = {
            'form': form,
            'first_coefficient': first_coefficient,
            'second_coefficient': second_coefficient,
            'third_coefficient': third_coefficient,
        }

        return render(request, 'quadratic_equation.html', context)

    def post(self, request):
        submit_button = request.POST.get("submit", )
        first_coefficient = ''
        second_coefficient = ''
        third_coefficient = ''
        form = CalculatorForm(request.POST or None)
        if form.is_valid():
            first_coefficient = form.cleaned_data.get("first_coefficient", )
            second_coefficient = form.cleaned_data.get("second_coefficient", )
            third_coefficient = form.cleaned_data.get("third_coefficient", )

        context = {
            'form': form,
            'first_coefficient': first_coefficient,
            'second_coefficient': second_coefficient,
            'third_coefficient': third_coefficient,
            'submit_button': submit_button,
        }
        return self.calculate(context, request)

    def calculate(self, context, request):
        try:
            a = float(context['first_coefficient'])
            b = float(context['second_coefficient'])
            c = float(context['third_coefficient'])

            discr = b ** 2 - 4 * a * c
            if discr > 0:
                answer = f'X1 = {-b + discr ** 0.5 / 2 * a}\nX2 = {-b - discr ** 0.5 / 2 * a}'
                return render(request, 'quadratic_equation.html', {'answer': answer, **context})

            elif discr == 0:
                if a == 0:
                    answer = 'Коэффициент "а" не может быть равен нулю'
                    return render(request, 'quadratic_equation.html', {'answer': answer, **context})
                else:
                    if not b == 0:
                        answer = f'X = {-b / 2 * a}'
                        return render(request, 'quadratic_equation.html', {'answer': answer, **context})
                    else:
                        answer = f'X = {(-b / 2 * a) * -1}'
                        return render(request, 'quadratic_equation.html', {'answer': answer, **context})
            else:
                answer = "Уравнение не имеет решения"
                return render(request, 'quadratic_equation.html', {'answer': answer, **context})
        except:
            answer = 'Обязательно использование целых чисел и дробных чисел разделенных "."'
            return render(request, 'quadratic_equation.html', {'answer': answer, **context})



class Color(TemplateView):
    template_name = 'color.html'

    def get(self, request, **kwargs):
        number = ''
        form = ColorForm(request.POST or None)
        if form.is_valid():
            print('FORM IS VALID')
        context = {
            'form': form,
            'number': number,
        }

        return render(request, 'color.html', context)

    def post(self, request):
        submit_button = request.POST.get("submit", )
        number = ''
        form = ColorForm(request.POST or None)
        if form.is_valid():
            number = form.cleaned_data.get("number", )

        context = {
            'form': form, 'number': number, 'submit_button': submit_button,
        }
        return self.guess(context, request)

    def guess(self, context, request):
        values = ['blue', 'green', 'red']
        try:
            number = int(context['number'])
            if number > 100 or number < 1 or not isinstance(number, int):
                error = 'Вы ввели недопустимое значение'
                return render(request, 'color.html', {'error': error, **context})
            else:
                data = random.choices(values, weights=[0.55, 0.25, 0.20], k=1)
                color = str(data[0])
                return render(request, 'color.html', {'color': color, **context})
        except:
            error = 'Вы ввели недопустимое значение'
            return render(request, 'color.html', {'error': error, **context})
