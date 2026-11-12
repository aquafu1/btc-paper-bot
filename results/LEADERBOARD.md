# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 110 windows, 2827 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 217 | 60.8 | 52.9 | $+280.14 | +12.9% | $1280.14 | +2.0 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 274 | 55.5 | 51.9 | $+132.15 | +4.8% | $1132.15 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 433 | 53.1 | 50.8 | $+42.49 | +1.0% | $1042.49 | +0.2 | done | can't tell from luck |
| value_ev10 | 145 | 40.0 | 40.7 | $-89.56 | -6.2% | $910.44 | -0.6 | Thu 8:30 AM | too few trades (145/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 2:15 PM | too few trades (50/200) |
| value_ev5 | 202 | 38.1 | 42.0 | $-259.16 | -12.8% | $740.84 | -1.6 | done | can't tell from luck |
| trend_filter | 149 | 41.6 | 49.1 | $-268.02 | -18.0% | $731.98 | -2.2 | Thu 7:15 AM | too few trades (149/200) |
| coinflip | 433 | 49.9 | 51.4 | $-282.12 | -6.5% | $717.88 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 274 | 44.5 | 50.2 | $-386.42 | -14.1% | $613.58 | -2.4 | done | losing for real |
| always_up | 433 | 47.1 | 50.3 | $-423.14 | -9.8% | $576.86 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 217 | 39.2 | 49.2 | $-489.02 | -22.5% | $510.98 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 616 | 45.8 | 49.7 | $-548.44 |
| ETH | 686 | 45.8 | 49.0 | $-628.19 |
| SOL | 753 | 48.9 | 48.6 | $-399.41 |
| XRP | 772 | 50.3 | 49.2 | $-290.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
