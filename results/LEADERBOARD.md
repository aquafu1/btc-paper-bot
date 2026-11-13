# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 251 windows, 6603 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 654 | 55.8 | 52.2 | $+168.15 | +2.6% | $1168.15 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 526 | 53.2 | 52.1 | $-106.44 | -2.0% | $893.56 | -0.5 | done | can't tell from luck |
| value_ev20 | 118 | 33.1 | 36.7 | $-160.27 | -13.6% | $839.73 | -1.2 | Sun 9:45 AM | too few trades (118/200) |
| trend_filter | 347 | 46.4 | 50.6 | $-430.99 | -12.4% | $569.01 | -2.4 | done | losing for real |
| value_ev10 | 316 | 36.4 | 40.8 | $-453.26 | -14.3% | $546.74 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 526 | 46.8 | 50.0 | $-594.11 | -11.3% | $405.89 | -2.7 | done | losing for real |
| value_ev5 | 465 | 38.7 | 42.5 | $-605.11 | -13.0% | $394.89 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 999 | 50.1 | 51.6 | $-731.81 | -7.3% | $268.19 | -2.4 | done | losing for real |
| coinflip | 999 | 49.3 | 50.9 | $-769.94 | -7.7% | $230.06 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 654 | 44.2 | 49.9 | $-1014.54 | -15.5% | $-14.54 | -4.1 | done | losing for real |
| always_up | 999 | 46.6 | 50.4 | $-1204.84 | -12.1% | $-204.84 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1473 | 46.4 | 49.8 | $-1585.20 |
| ETH | 1646 | 46.7 | 49.1 | $-1735.92 |
| SOL | 1712 | 48.0 | 49.4 | $-1492.97 |
| XRP | 1772 | 48.5 | 49.2 | $-1089.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
