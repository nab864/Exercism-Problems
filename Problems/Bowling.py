

'''
Frame Object requirements:
    1. store each throw (data)
    2. calculate total points for the frame (method)
    3. determine if the frame includes a strike or spare (method)
    4. know when the frame is full (method)
    5. be able to adjust for the 10th frame since it is a special case (method)
'''
class Frame:
    def __init__(self, num):
        self.num = num
        self.throws = []

    ''' 
    @property lets me check the boolean within def is_done(self) everytime I call self.is_done outside of the Frame Object
    without creating a variable self.is_done on init.
    '''
    @property
    def is_done(self):
        if self.is_10th_frame():
            if self.is_strike() or self.is_spare():
                return len(self.throws) == 3
            else:
                return len(self.throws) == 2
        else:
            return sum(self.throws) == 10 or len(self.throws) == 2
    def is_strike(self):
        if self.is_10th_frame():
            try:
                return self.throws[0] == 10
            except:
                pass
        return sum(self.throws) == 10 and len(self.throws) == 1
    def is_spare(self):
        if self.is_10th_frame():
            try:
                return sum(self.throws[0:2]) == 10
            except:
                pass
        return sum(self.throws) == 10 and len(self.throws) == 2
    def is_10th_frame(self):
        return self.num == 9

    def frame_score(self, next_throws):
        if self.is_strike():
            next_two_sum = sum(next_throws[:2])
            return sum(self.throws) + next_two_sum
        elif self.is_spare():
            next_sum = sum(next_throws[:1])
            return sum(self.throws) + next_sum
        else:
            return sum(self.throws)

    def add_to_frame(self, pins):
        self.throws.append(pins)

'''
Bowling Object Requirements:
    1. list of 10 Frames
    2. throw the ball and tell the current Frame how many pins were hit {def add_to_frame()}
    3. move to the next Frame when the current Frame says it is done {def is_done()}
    4. if a Frame has a strike or a spare, Bowling will tell Frame what the next 1 or 2 throws are.
    5. add up all of the Frames.frame_score()
    6. show Frame.frame_score as a list next to the total current score
'''
class Bowling:
    def __init__(self):
        self.all_frames = [Frame(i) for i in range(10)]
        self.current_frame = 0

    def next_frame(self):
        self.current_frame += 1

    def get_current_frame(self):
        return self.all_frames[self.current_frame]

    '''
    next_throw_list() is used to add the additional throws for strikes and spares
    '''
    def next_throw_list(self, frame_num):
        throw_list = []
        next_frame_num = frame_num + 1
        while next_frame_num < 10:
            throw_list += self.all_frames[next_frame_num].throws
            next_frame_num += 1
        return throw_list

    def throw_ball(self, pins_hit):

        if not self.get_current_frame().is_done:
            if pins_hit + sum(self.get_current_frame().throws) > 10:
                raise ValueError('Too many pins than what is left')

            self.get_current_frame().add_to_frame(pins_hit)
            self.show_score()
        else:
            self.next_frame()
            self.throw_ball(pins_hit)


    def get_total(self):
        total_score = 0
        for frame in self.all_frames:
            total_score += frame.frame_score(self.next_throw_list(frame.num))
        return total_score

    def show_score(self):
        print([frame.frame_score(self.next_throw_list(frame.num)) for frame in self.all_frames if frame.throws != []],
              self.get_total())

