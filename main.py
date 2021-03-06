# Copyright 2020 Diogo Coelho
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Standard library imports
import os
from random import randint
# Third party imports
from getch import pause


RESPOSTAS1 = ("It is certain.", 'It is decidedly so.','Yes - definitely.', 'You may rely on it.', 'As I see it, yes.')
RESPOSTAS2 = ("Most likely.", 'Outlook good.','Yes.', 'Signs point to yes.', 'Without a doubt.')
RESPOSTAS3 = ("Reply hazy, try again.", 'Ask again later.','Better not tell you now.', 'Cannot predict now.', ' Concentrate and ask again.')
RESPOSTAS4 = (" Don't count on it.", ' My reply is no.','My sources say no.', 'Outlook not so good.', 'Very doubtful')

RESPOSTAS = (RESPOSTAS1, RESPOSTAS2, RESPOSTAS3, RESPOSTAS4)


def main():
    while True:
        os.system('cls')
        pause('What do you wanna know?')
        i = randint(0, 3)
        j = randint(0, 4)
        pause(RESPOSTAS[i][j])

if __name__=="__main__":
    main()
