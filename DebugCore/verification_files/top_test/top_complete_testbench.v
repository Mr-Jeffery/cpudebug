`timescale 1ns / 1ps

module top_complete_testbench ();
    reg clk = 0, rst_n = 1;
    wire uart_in_progress = 0, hsync = 0, vsync = 0, uart_tx = 0;
    reg [3:0] row_in = 4'b1111;
    wire [3:0] col_out = 0;
    wire [7:0] seg_tube = 0, seg_enable = 0;
    wire [11:0] vga_signal = 0;
    
    top uut(
    .clk_raw(clk), .rst_n(rst_n),
    .switch_map(8'b1111_1111),
    .uart_rx(1'b0),
    .row_in(row_in),
    .col_out(col_out),
    .seg_tube(seg_tube),   
    .seg_enable(seg_enable),
    .vga_signal(vga_signal),
    .uart_in_progress(uart_in_progress),
    .hsync(hsync), 
    .vsync(vsync),
    .uart_tx(uart_tx)
    );

    always begin
        #5 clk = ~clk;
    end

    initial begin
        #5 rst_n = 0;
        #5 rst_n = 1;

        //  col_out: 4'b0111
            row_in = 4'b1111; // none
        #2500010
        //  col_out: 4'b1011
            row_in = 4'b1110; // three
            // row_in = 4'b1111; // none
        #2500010
        //  col_out: 4'b1101
            row_in = 4'b1111; // none
            // row_in = 4'b1110; // two
        #2500010
        //  col_out: 4'b1110
            row_in = 4'b1110; // one
            // row_in = 4'b1111; // none
        #2500010 
        //  col_out: 4'b0111
            row_in = 4'b1111; // none
        #2500010 
        //  col_out: 4'b1011
            row_in = 4'b1111; // none
        
        while (col_out != 4'b0111) #2500010 row_in = 4'b1111; // until next cycle

        //  col_out: 4'b0111
            row_in = 4'b1111; // none
        #2500010
        //  col_out: 4'b1011
            row_in = 4'b0111; // enter
        #2500010
        //  col_out: 4'b1101
            row_in = 4'b1111; // none
        
        while (col_out != 4'b0111) #2500010 row_in = 4'b1111;
        
        // #10000040
        #2500010
            // row_in = 4'b1110; // one
            row_in = 4'b1111;
        #2500010
            row_in = 4'b1111;
        #2500010
            row_in = 4'b0111;
        #2500010
            row_in = 4'b1111;
        
        // #2500000
        // #2500000
            // row_in = 4'b1110;
        
        #10000040
        #2500010
            row_in = 4'b1101;
        #2500010
            row_in = 4'b1111;
        #2500010
            row_in = 4'b0111;
        #2500010
            row_in = 4'b1111;
        
        #10000040
        #2500010
            row_in = 4'b1110;
        #2500010
            row_in = 4'b1111;
        #2500010
            row_in = 4'b0111;
        #2500010
            row_in = 4'b1111;
        
        #10000040
        #2500010
            row_in = 4'b1110;
        #2500010
            row_in = 4'b1111;
        #2500010
            row_in = 4'b0111;
        #2500010
            row_in = 4'b1111;
        #10000040
        #2500010
            row_in = 4'b1011;
        #2500010
            row_in = 4'b1111;
        #2500010
            row_in = 4'b0111;
        #2500010
            row_in = 4'b1111;
    end

endmodule