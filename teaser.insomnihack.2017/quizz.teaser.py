#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import socket

def netcat(hostname, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hostname, port))
	while 1:
		data = s.recv(1024)
		if data.decode('utf-8') == "":
			break
		for d in data.decode('utf-8').split('\n'):
			pref = "What is the birth year of "
			if d.find(pref) != -1:
				x = d.split(pref)[1].split("?")[0][:-1]
				if x in names:
					print(birthdate[names.index(x)])   
					Message = "%s" % birthdate[names.index(x)]
					s.send(bytes(Message+"\n", "UTF-8"))   		
	s.close()

names = ["Amos Fiat", "Donald Davies", "Shai Halevi", "Nigel P. Smart", "Paul van Oorschot", "Lars Knudsen", "Antoine Joux", "Daniel J. Bernstein", "Ralph Merkle", "Mitsuru Matsui", "Yvo Desmedt", "Victor S. Miller", "Jacques Stern", "Xuejia Lai", "Moni Naor", "Whitfield Diffie", "Niels Ferguson", "Michael O. Rabin", "Daniel Bleichenbacher", "Serge Vaudenay", "Markus Jakobsson", "Paul Kocher", "Martin Hellman", "Ron Rivest", "Paulo Barreto", "David Naccache", "Ross Anderson", "Kaisa Nyberg", "Phil Rogaway", "Douglas Stinson", "Horst Feistel", "Jacques Patarin", "Rafail Ostrovsky", "Ronald Cramer", "Yehuda Lindell", "Alex Biryukov", "Daniel J. Bernstein", "Joan Daemen", "Jim Massey", "Adi Shamir"]
birthdate = ["1956", "1924", "1966", "1967", "1962", "1962", "1967", "1970", "1952", "1961", "1956", "1947", "1949", "1954", "1961", "1944", "1965", "1931", "1964", "1968", "1968", "1973", "1945", "1947", "1965", "1967", "1956", "1948", "1962", "1956", "1915", "1965", "1963", "1968", "1971", "1969", "1971", "1965", "1934", "1952"]
#nc quizz.teaser.insomnihack.ch 1031
netcat("quizz.teaser.insomnihack.ch", 1031)
