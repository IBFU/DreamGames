class com.transitions.BgTween
{
    var target, friction, rate;
    function BgTween(target, bg_width, speed, friction)
    {
        this.target = target;
        speedX = speed;
        this.friction = friction;
        centerX = Stage.width / 2;
        rate = (bg_width - Stage.width) / 2 / centerX;
    } // End of the function
    function moving()
    {
        dx = (centerX - _xmouse) * rate;
        if (target._x > dx)
        {
            speedX = Math.abs(target._x - dx) * friction;
            target._x = target._x - speedX;
        }
        else
        {
            speedX = Math.abs(target._x - dx) * friction;
            target._x = target._x + speedX;
        } // end else if
    } // End of the function
	    function mov(bool)
    {
        if(bool){
            dx = (centerX - _xmouse) * rate;
            if (target._x > dx)
            {
                speedX = Math.abs(target._x - dx) * friction;
                target._x = target._x - speedX;
            }
            else
            {
                speedX = Math.abs(target._x - dx) * friction;
                target._x = target._x + speedX;
            } // end else if
        }
    } // End of the function
    var centerX = 0;
    var speedX = 8;
    var dx = 0;
} // End of Class
