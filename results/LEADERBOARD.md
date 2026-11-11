# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 87 windows, 2206 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 340 | 56.8 | 50.9 | $+285.93 | +8.4% | $1285.93 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 162 | 59.9 | 52.9 | $+174.25 | +10.8% | $1174.25 | +1.4 | Wed 5:30 PM | too few trades (162/200) |
| reversal_15m_0.10pct | 212 | 55.2 | 52.3 | $+75.60 | +3.6% | $1075.60 | +0.5 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 4:00 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 6:15 PM | too few trades (43/200) |
| trend_filter | 120 | 47.5 | 48.7 | $-65.31 | -5.4% | $934.69 | -0.6 | Thu 2:45 AM | too few trades (120/200) |
| value_ev5 | 159 | 40.3 | 41.6 | $-118.55 | -7.5% | $881.45 | -0.8 | Wed 6:00 PM | too few trades (159/200) |
| coinflip | 340 | 49.7 | 51.5 | $-227.18 | -6.7% | $772.82 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 212 | 44.8 | 49.5 | $-259.52 | -12.2% | $740.48 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 162 | 40.1 | 48.7 | $-323.03 | -19.9% | $676.97 | -2.5 | Wed 5:30 PM | too few trades (162/200) |
| always_up | 340 | 45.9 | 50.1 | $-387.50 | -11.4% | $612.50 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 475 | 48.4 | 49.8 | $-104.09 |
| ETH | 536 | 46.8 | 48.6 | $-286.14 |
| SOL | 589 | 49.9 | 48.5 | $-185.27 |
| XRP | 606 | 49.7 | 48.7 | $-326.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
