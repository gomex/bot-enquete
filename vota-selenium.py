#!/usr/bin/env python2
# -*- coding: utf-8 -*-

''' by AllanDaemon copyleft CC0 (Public Domain)'''

from __future__ import print_function

from time import sleep
from selenium import webdriver

url = 'http://sepoppesquisa.senado.gov.br/mrIWeb/mrIWeb.dll?I.Project=E012ENQUETEMAIOJUNHODE2016'
timeSleep = 3

#########
isError = lambda b: b.title == 'Interviewer Server - Error'

def handleError(b):
	while isError(b):
		sleep(timeSleep)
		b.refresh()

#########

def vota():

	# b = webdriver.Chrome()
	# b = webdriver.Firefox()
	b = webdriver.PhantomJS('./phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

	b.implicitly_wait(10)
	b.get(url)


	# primeira tela

	handleError(b)
	while b.title != 'Enquete DataSenado':
		b.get(url)
		handleError(b)

	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("span.mrQuestionText")
	assert elem.text.startswith(u'As pr\xf3ximas p\xe1ginas cont\xeam perguntas sobre a proposta de proibi\xe7\xe3o')

	elem = b.find_element_by_xpath('//div[@id="buttons"]/input[@type="submit"]')
	elem.click()

	## pergunta 1

	handleError(b)
	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("span.mrQuestionText")
	assert elem.text.startswith("Atualmente, o consumo de internet")

	elem = b.find_element_by_xpath('//input[@value="Contra"]')
	elem.click()

	elem = b.find_element_by_xpath('//div[@id="buttons"]/input[@type="submit"][@name="_NNext"]')
	elem.click()


	## pergunta 2

	handleError(b)
	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("span.mrQuestionText")
	assert elem.text == u'Em sua opini\xe3o, com a limita\xe7\xe3o do consumo de dados na internet de banda larga fixa:'

	# table = b.find_element_by_css_selector("table.mrQuestionTable")

	elem = b.find_element_by_xpath(u'//input[@name="_QP02_QA__satisfação__dos_QGV1_C"][@value="Diminuir"]')
	elem.click()

	elem = b.find_element_by_xpath('//input[@name="_QP02_QA__qualidade__dos___QGV1_C"][@value="Diminuir"]')
	elem.click()

	elem = b.find_element_by_xpath('//input[@name="_QP02_QOs__gastos__dos__cl_QGV1_C"][@value="Aumentar"]')
	elem.click()

	elem = b.find_element_by_xpath('//input[@name="_QP02_QO__lucro__das__empr_QGV1_C"][@value="Aumentar"]')
	elem.click()

	elem = b.find_element_by_xpath('//div[@id="buttons"]/input[@type="submit"][@name="_NNext"]')
	elem.click()

	## pergunta 3

	handleError(b)
	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("span.mrQuestionText")
	assert elem.text.startswith("A Lei 12.965/2014, conhecida como Marco Civil da Internet,")

	# elem = b.find_element_by_xpath(u'//input[@name="_QP03_C"][@value="Não__sei__ou__prefi"]')
	elem = b.find_element_by_xpath(u'//input[@name="_QP03_C"][@value="Não__está__de__acor"]')
	elem.click()

	elem = b.find_element_by_xpath('//div[@id="buttons"]/input[@type="submit"][@name="_NNext"]')
	elem.click()


	## pergunta 4

	handleError(b)
	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("span.mrQuestionText")
	assert elem.text == u'Voc\xea \xe9 a favor ou contra o bloqueio coletivo de aplicativos de comunica\xe7\xe3o por decis\xf5es judiciais?'


	# elem = b.find_element_by_xpath(u'//input[@name="_QP05_C"][@value="Não__sei__ou__prefi"]')
	elem = b.find_element_by_xpath('//input[@name="_QP05_C"][@value="Contra"]')
	elem.click()

	elem = b.find_element_by_xpath('//div[@id="buttons"]/input[@type="submit"][@name="_NNext"]')
	elem.click()

	## final
	handleError(b)
	assert b.title == 'Enquete DataSenado'
	elem = b.find_element_by_css_selector("#cont-body > div > h2")
	assert elem.text == 'A enquete foi finalizada.'

	b.close()


if __name__ == '__main__':
	from itertools import count
	from sys import stdout

	err = 0
	for i in count(1):
		try:
			vota()
		except KeyboardInterrupt:
			print('\nTotal de votos: ', i-err)
			break
		except:
			print("Ops!")
			err += 1
		print('\rVotos: ', i, end='')
		stdout.flush()
