class com.transitions.BgHigh
{
    var target, friction, rate;
    function BgHigh(target, bg_width, speed, friction)
    {
        this.target = target;
        speedX = speed;
        this.friction = friction;
        centerX = Stage.height / 2;
        rate = (bg_width - Stage.height) / 2 / centerX;
    } // End of the function
    function moving()
    {
        dx = (centerX - _ymouse) * rate;
        if (target._y > dx)
        {
            speedX = Math.abs(target._y - dx) * friction;
            target._y = target._y - speedX;
        }
        else
        {
            speedX = Math.abs(target._y - dx) * friction;
            target._y = target._y + speedX;
        } // end else if
    } // End of the function
    function mov(bool)
    {
        if(bool){
            dx = (centerX - _ymouse) * rate;
            if (target._y > dx)
            {
                speedX = Math.abs(target._y - dx) * friction;
                target._y = target._y - speedX;
            }
            else
            {
                speedX = Math.abs(target._y - dx) * friction;
                target._y = target._y + speedX;
            } // end else if
        }
    } // End of the function
    var centerX = 0;
    var speedX = 8;
    var dx = 0;
} // End of Class
