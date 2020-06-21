from pysine import sine

max_pi_range = 100000000000

notes = [261.63,293.66,329.63,349.23,392.00,440.00,493.88,523.25,587.33,659.25]

fibo_seq = [5,8,13,21]

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(max_pi_range):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


#my_array = []

#for i in make_pi():
    #my_array.append(str(i))

#my_array = my_array[:1] + ['.'] + my_array[1:]
#pi_string = "".join(my_array)
#pi_string = pi_string[2:]
pi_generator = make_pi()
fibo_seq_index = 0
pi_string_index = 0


while True:

    beat_count = fibo_seq[fibo_seq_index]

    if fibo_seq_index == len(fibo_seq)-1:
        fibo_seq_increment = -1
    elif fibo_seq_index == 0:
        fibo_seq_increment = 1

    fibo_seq_index += fibo_seq_increment

    if pi_string_index + beat_count >= max_pi_range -1:
        print("Pi is exhausted! Music over")
        break
    else:
        temp_notes = []
        for i in range(beat_count):
            temp_notes.append(next(pi_generator)) # = pi_string[pi_string_index:(pi_string_index+beat_count)]

    for note_val in temp_notes:
        sine(frequency=notes[int(note_val)], duration=0.45)

    pi_string_index = pi_string_index+beat_count

    sine(frequency=0, duration=1)