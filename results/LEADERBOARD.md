# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 85 windows, 2157 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 332 | 56.0 | 50.8 | $+233.85 | +7.0% | $1233.85 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 158 | 59.5 | 52.9 | $+156.43 | +9.9% | $1156.43 | +1.3 | Wed 5:45 PM | too few trades (158/200) |
| reversal_15m_0.10pct | 205 | 56.6 | 52.2 | $+128.87 | +6.3% | $1128.87 | +0.9 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 3:15 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 4:00 PM | too few trades (43/200) |
| trend_filter | 118 | 46.6 | 48.6 | $-83.05 | -7.0% | $916.95 | -0.7 | Thu 2:30 AM | too few trades (118/200) |
| value_ev5 | 158 | 40.5 | 41.5 | $-108.55 | -6.9% | $891.45 | -0.7 | Wed 5:45 PM | too few trades (158/200) |
| coinflip | 332 | 50.0 | 51.5 | $-202.62 | -6.1% | $797.38 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 158 | 40.5 | 48.6 | $-303.47 | -19.2% | $696.53 | -2.4 | Wed 5:45 PM | too few trades (158/200) |
| momentum_15m_0.10pct | 205 | 43.4 | 49.5 | $-305.26 | -14.9% | $694.74 | -2.1 | done | losing for real |
| always_up | 332 | 46.7 | 50.0 | $-324.24 | -9.8% | $675.76 | -1.8 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 465 | 48.0 | 49.7 | $-130.06 |
| ETH | 524 | 47.1 | 48.5 | $-243.57 |
| SOL | 577 | 49.9 | 48.4 | $-180.92 |
| XRP | 591 | 49.7 | 48.6 | $-310.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
