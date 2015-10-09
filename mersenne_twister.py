from datetime import datetime


class MersenneTwister(object):

    def __init__(self,client_process_id,num_of_request=1):
        self.m_prime=1812433253
        self.dflt_indx = 624
        self.bit_opr = (2 ** 32) -1
        self.counter = 0
        self.num_of_requst = num_of_request

        self.seed = self.generate_seed(client_process_id)
        self.mt_array = self.init_mersenne_array(self.seed)

    def init_mersenne_array(self,seed):
        mt_temp = [0] * self.dflt_indx
        mt_temp[0] = seed
        for i in range(1,self.dflt_indx):
            mt_temp[i] = ((self.m_prime  * mt_temp[i-1]) ^ ((mt_temp[i-1] >> 30) + 1))

        return mt_temp

    def generate_seed(self,process_id):
        now = datetime.now()
        return now.microsecond + process_id

    def rand(self):
        list_of_rand=[]
        for i in range(self.num_of_requst):
            list_of_rand.append(self.get_random_number())

        return self.convert_to_hex(list_of_rand)

    def get_random_number(self):
        if self.counter == 0:
            self.mersenne_twist()
        rand_num = self.mt_array[self.counter]
        rand_num ^= rand_num >> 11
        rand_num ^= (rand_num << 7) & 2636928640
        rand_num ^= (rand_num << 15) & 4022730752
        rand_num ^= rand_num >> 18

        self.counter = (self.counter + 1) % self.dflt_indx
        return rand_num

    def mersenne_twist(self):
        for i in range(self.dflt_indx):
            y = (self.mt_array[i] & 0x8000000) + (self.mt_array[(i+1) % self.dflt_indx] & 0x7fffffff)
            self.mt_array[i] = self.mt_array[(i + 397) % self.dflt_indx] ^ (y >> 1)
            if y % 2 !=0:
                self.mt_array[i] ^= 0x9908b0df

    def convert_to_hex(self,num_list):
        return ''.join([hex(x) for x in num_list])
