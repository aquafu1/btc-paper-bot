# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 387 windows, 10561 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 10:45 PM | too few trades (196/200) |
| value_ev10 | 507 | 40.0 | 40.5 | $-209.23 | -4.1% | $790.77 | -0.8 | done | can't tell from luck |
| value_ev5 | 748 | 41.7 | 42.1 | $-328.33 | -4.4% | $671.67 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 889 | 50.1 | 49.8 | $-340.69 | -3.8% | $659.31 | -1.2 | done | can't tell from luck |
| trend_filter | 592 | 48.8 | 50.5 | $-453.13 | -7.7% | $546.87 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1060 | 49.0 | 49.7 | $-550.94 | -5.2% | $449.06 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1060 | 51.0 | 52.1 | $-634.18 | -6.0% | $365.82 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 889 | 49.9 | 52.1 | $-708.17 | -8.0% | $291.83 | -2.5 | done | losing for real |
| coinflip | 1540 | 49.9 | 50.8 | $-829.81 | -5.4% | $170.19 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1540 | 49.5 | 51.5 | $-1155.22 | -7.5% | $-155.22 | -3.0 | done | losing for real |
| always_up | 1540 | 45.9 | 50.7 | $-2007.54 | -13.0% | $-1007.54 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2386 | 47.5 | 49.4 | $-1762.90 |
| ETH | 2653 | 47.7 | 48.9 | $-1859.51 |
| SOL | 2734 | 47.9 | 49.5 | $-2100.14 |
| XRP | 2788 | 48.6 | 49.2 | $-1521.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
