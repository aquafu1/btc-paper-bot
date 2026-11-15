# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 402 windows, 11020 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 1:15 AM | too few trades (199/200) |
| value_ev10 | 519 | 40.5 | 40.5 | $-174.41 | -3.4% | $825.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 937 | 50.8 | 49.8 | $-200.92 | -2.1% | $799.08 | -0.7 | done | can't tell from luck |
| value_ev5 | 780 | 42.1 | 42.2 | $-293.06 | -3.8% | $706.94 | -0.9 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1108 | 49.5 | 49.8 | $-445.80 | -4.0% | $554.20 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1108 | 50.5 | 52.0 | $-749.94 | -6.8% | $250.06 | -2.4 | done | losing for real |
| coinflip | 1602 | 50.1 | 50.9 | $-793.81 | -5.0% | $206.19 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 937 | 49.2 | 52.1 | $-860.57 | -9.2% | $139.43 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1602 | 50.0 | 51.6 | $-1036.06 | -6.5% | $-36.06 | -2.7 | done | losing for real |
| always_up | 1602 | 45.9 | 50.8 | $-2053.22 | -12.8% | $-1053.22 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2484 | 47.8 | 49.5 | $-1687.96 |
| ETH | 2766 | 47.9 | 49.0 | $-1698.13 |
| SOL | 2852 | 48.0 | 49.5 | $-2087.91 |
| XRP | 2918 | 48.9 | 49.3 | $-1495.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
