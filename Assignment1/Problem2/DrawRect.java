import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DrawRect extends JPanel {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	//LeftTop, RightTop, RightB, LeftB
    int x1, y1, x2, y2, x3, y3, x4, y4;
    int x5, y5, x6, y6;
    int deltaX, deltaY;
    boolean hasRect = false;
    RadioPanel showPanel;
    
    DrawRect() {
        x1 = y1 = x2 = y2 = 0; // 
        x5 = y5 = x6 = y6 = 0;
        deltaX = deltaY = 0;
        MyMouseListener listener = new MyMouseListener();
        addMouseListener(listener);
        addMouseMotionListener(listener);
    }

    public void setStartPoint(int x, int y) {
        this.x1 = x;
        this.y1 = y;
    }

    public void setEndPoint(int x, int y) {
        this.x3 = x;
        this.y3 = y;
    }
    public void setModifyStartPoint(int x, int y) {
        this.x5 = x;
        this.y5 = y;
    }

    public void setModifyEndPoint(int x, int y) {
        x6 = x;
        y6 = y;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        ((Graphics2D)g).setStroke(new BasicStroke(3));
        if (hasRect == false) {
            int xmin = Math.min(x1,x3);
            int ymin = Math.min(y1,y3);
            int xmax = Math.max(x1, x3);
            int ymax = Math.max(y1, y3);
            x1 = xmin;
            y1 = ymin;
            x2 = xmax;
            y2 = ymin;
            x3 = xmax;
            y3 = ymax;
            x4 = xmin;
            y4 = ymax;

            
            g.drawRect(x1, y1, x3 - x1, y3 - y1);
        }
        else {
	        // 1. translation deltaX = Move(x) deltaY = Move(y)
			if (RadioPanel.getSelected() == 1) {    
				g.drawRect(x1 + deltaX, y1 + deltaY, x3 - x1, y3 - y1 );
			}
			
			// 2. rigid deltaX = Move(x) deltaY = Move(y); rot arctan(deltaY/deltaX)
			if (RadioPanel.getSelected() == 2) {  
				try {
					// get center
					int centerX = (x1 + x2)/2;
					int centerY = (y1 + y4)/2;
					
					// get rotation angle
					double theta = 0;

					theta = Math.atan(-(double)deltaY/(double)deltaX);
					//System.out.println("theta: " + theta + "dX: " + deltaX + "dY: " + deltaY +"\n");

					// rotate + translate
					int xlt = (int) ( (x1 - centerX) * Math.cos(theta) + (y1 - centerY) * Math.sin(theta)) + centerX + deltaX;
					int ylt = (int) (-(x1 - centerX) * Math.sin(theta) + (y1 - centerY) * Math.cos(theta)) + centerY + deltaY;
					
					int xrt = (int) ( (x2 - centerX) * Math.cos(theta) + (y2 - centerY) * Math.sin(theta)) + centerX + deltaX;
					int yrt = (int) (-(x2 - centerX) * Math.sin(theta) + (y2 - centerY) * Math.cos(theta)) + centerY + deltaY;
				
					int xrb = (int) ( (x3 - centerX) * Math.cos(theta) + (y3 - centerY) * Math.sin(theta)) + centerX + deltaX;
					int yrb = (int) (-(x3 - centerX) * Math.sin(theta) + (y3 - centerY) * Math.cos(theta)) + centerY + deltaY;
					
					int xlb = (int) ( (x4 - centerX) * Math.cos(theta) + (y4 - centerY) * Math.sin(theta)) + centerX + deltaX;
					int ylb = (int) (-(x4 - centerX) * Math.sin(theta) + (y4 - centerY) * Math.cos(theta)) + centerY + deltaY;
					
					int[] xPoly = {xlt, xrt, xrb, xlb};
					int[] yPoly = {ylt, yrt, yrb, ylb};
					
					g.drawPolygon(xPoly, yPoly, 4);
				}catch ( Exception e) {
					
				}
			}
			// 3. similarity deltaX = Move(x) deltaY = Move(y); rot arctan(deltaY/deltaX) scale = min(scaleX,scaleY)
			// scaleX: (x+deltaX)/x
			if (RadioPanel.getSelected() == 3) {  
				try {
					// get center
					int centerX = (x1 + x2)/2;
					int centerY = (y1 + y4)/2;
					
					// get rotation angle
					double theta = Math.atan(-(double)deltaY/(double)deltaX);
					
					// get scale
					double scaleX = (double)x6/(double)x5;
					double scaleY = (double)y6/(double)y5;
					double scale = (scaleX+ scaleY)/2;
					//System.out.println("Scale: " + scale + "X: " + scaleX + "Y: " + scaleY +"\n");
					
					// rotate * scale + translate
					int xlt = (int) (( (x1 - centerX) * Math.cos(theta) + (y1 - centerY) * Math.sin(theta))*scale) + centerX + deltaX;
					int ylt = (int) ((-(x1 - centerX) * Math.sin(theta) + (y1 - centerY) * Math.cos(theta))*scale) + centerY + deltaY;
					
					int xrt = (int) (( (x2 - centerX) * Math.cos(theta) + (y2 - centerY) * Math.sin(theta))*scale) + centerX + deltaX;
					int yrt = (int) ((-(x2 - centerX) * Math.sin(theta) + (y2 - centerY) * Math.cos(theta))*scale) + centerY + deltaY;
				
					int xrb = (int) (( (x3 - centerX) * Math.cos(theta) + (y3 - centerY) * Math.sin(theta))*scale) + centerX + deltaX;
					int yrb = (int) ((-(x3 - centerX) * Math.sin(theta) + (y3 - centerY) * Math.cos(theta))*scale) + centerY + deltaY;
					
					int xlb = (int) (( (x4 - centerX) * Math.cos(theta) + (y4 - centerY) * Math.sin(theta))*scale) + centerX + deltaX;
					int ylb = (int) ((-(x4 - centerX) * Math.sin(theta) + (y4 - centerY) * Math.cos(theta))*scale) + centerY + deltaY;
					
					int[] xPoly = {xlt, xrt, xrb, xlb};
					int[] yPoly = {ylt, yrt, yrb, ylb};
					
					g.drawPolygon(xPoly, yPoly, 4);
				}catch ( Exception e) {
					
				}
			
			}
			// 4. Affine

			if (RadioPanel.getSelected() == 4) {  
				try {

					int xlt = x1 + deltaX/2;
					int ylt = y1 - deltaY/2;
					
					int xrt = x2 + deltaX/2;
					int yrt = y2 + deltaY/2;
				
					int xrb = x3 - deltaX/2;
					int yrb = y3 + deltaY/2;
					
					int xlb = x4 - deltaX/2;
					int ylb = y4 - deltaY/2;
					
					int[] xPoly = {xlt, xrt, xrb, xlb};
					int[] yPoly = {ylt, yrt, yrb, ylb};
					
					g.drawPolygon(xPoly, yPoly, 4);
				}catch ( Exception e) {
					
				}
			
			}
			// 4. Perspective

			if (RadioPanel.getSelected() == 5) {  
				try {

					int xlt = x1 + deltaX/2;
					int ylt = y1 - deltaY/2;
					
					int xrt = x2 - deltaX/2;
					int yrt = y2 - deltaY/2;
				
					int xrb = x3 + deltaX/2;
					int yrb = y3 + deltaY/2;
					
					int xlb = x4 - deltaX/2;
					int ylb = y4 + deltaY/2;
					
					int[] xPoly = {xlt, xrt, xrb, xlb};
					int[] yPoly = {ylt, yrt, yrb, ylb};
					
					g.drawPolygon(xPoly, yPoly, 4);
				}catch ( Exception e) {
					
				}
			
			}
        }
		
		
		
		
		
		
    }
    
    class MyMouseListener extends MouseAdapter {

        public void mousePressed(MouseEvent e) {
        	if (MyKeyListener.isShiftDown()) {
        		hasRect = false;
        		deltaX = 0;
        		deltaY = 0;
        		setStartPoint(e.getX(), e.getY());
        	}
        	if (hasRect) {
        		setModifyStartPoint(e.getX(), e.getY());
        	}
        }

        public void mouseDragged(MouseEvent e) {
        	if (hasRect) {
        		setModifyEndPoint(e.getX(), e.getY());
        		deltaX = x6 - x5;
        		deltaY = y6 - y5;
        		repaint();
        	}
        	if (MyKeyListener.isShiftDown()) {
        		setEndPoint(e.getX(), e.getY());  
        		hasRect = false;
        		repaint();
        	}  

        }
        public void mouseReleased(MouseEvent e) {

        	if (MyKeyListener.isShiftDown()) {
        		setEndPoint(e.getX(), e.getY());
        		hasRect = true;
        		//repaint();
        	}  
        	
        }

    }
    static class RadioPanel extends JPanel{

		/**
		 * 
		 */
		private static final long serialVersionUID = 1L;
		static JRadioButton radio1 ;
    	static JRadioButton radio2 ;
    	static JRadioButton radio3 ;
    	static JRadioButton radio4 ;
    	static JRadioButton radio5 ;

    	RadioPanel() {
    		radio1 = new JRadioButton("translation", true);
    		radio2 = new JRadioButton("rigid");
    		radio3 = new JRadioButton("similarity");
    		radio4 = new JRadioButton("affine");
    		radio5 = new JRadioButton("perspective");
    	
    	   ButtonGroup group = new ButtonGroup();
    	   group.add(radio1);
    	   group.add(radio2);
    	   group.add(radio3);
    	   group.add(radio4);
    	   group.add(radio5);
    	
    	   add(radio1);
    	   add(radio2);
    	   add(radio3);
    	   add(radio4);
    	   add(radio5);
    	   setBorder(BorderFactory.createTitledBorder("Choices"));
       }
    	
    	public static int getSelected() {
    		if (radio1.isSelected()) {
    			return 1;
    		}
    		if (radio2.isSelected()) {
    			return 2;
    		}
    		if (radio3.isSelected()) {
    			return 3;
    		}
    		if (radio4.isSelected()) {
    			return 4;
    		}
    		if (radio5.isSelected()) {
    			return 5;
    		}
    		
    		return 0;
    	}
    }
    static class MyKeyListener{

        private static boolean isShiftDown;

        static {
            KeyboardFocusManager.getCurrentKeyboardFocusManager().addKeyEventDispatcher(
                new KeyEventDispatcher() {
                    public boolean dispatchKeyEvent(KeyEvent e) {
                        isShiftDown = e.isShiftDown();
                        return false;
                    }
                });
        }

        public static boolean isShiftDown() {
            return isShiftDown;
        }

    }
    
    public static void main(String[] args) {
        JFrame f = new JFrame("Draw Box Mouse 2");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // set layout
	    f.setLayout(new BorderLayout());
	    	DrawRect drawPanel = new DrawRect(); 
	    	RadioPanel showPanel = new RadioPanel();
	    	
	    f.add(showPanel, BorderLayout.NORTH);
        f.add(drawPanel, BorderLayout.CENTER);
        
        // initialize MyKey Listener by calling it.
       MyKeyListener.isShiftDown();
       RadioPanel.getSelected();
        f.setSize(600, 600);
        f.setVisible(true);
    }




}
