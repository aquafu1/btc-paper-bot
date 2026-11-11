# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 91 windows, 2311 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 356 | 56.2 | 50.9 | $+251.76 | +7.1% | $1251.76 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 173 | 59.0 | 52.7 | $+156.43 | +9.0% | $1156.43 | +1.3 | Wed 5:00 PM | too few trades (173/200) |
| reversal_15m_0.10pct | 222 | 55.9 | 52.3 | $+103.71 | +4.7% | $1103.71 | +0.7 | done | can't tell from luck |
| value_ev10 | 118 | 41.5 | 40.2 | $-23.12 | -2.0% | $976.88 | -0.2 | Thu 5:00 AM | too few trades (118/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 8:30 PM | too few trades (44/200) |
| trend_filter | 127 | 47.2 | 48.8 | $-84.96 | -6.7% | $915.04 | -0.7 | Thu 2:30 AM | too few trades (127/200) |
| value_ev5 | 164 | 39.0 | 41.7 | $-168.55 | -10.3% | $831.45 | -1.1 | Wed 6:30 PM | too few trades (164/200) |
| coinflip | 356 | 50.3 | 51.6 | $-208.48 | -5.9% | $791.52 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 222 | 44.1 | 49.5 | $-302.32 | -13.6% | $697.68 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 173 | 41.0 | 49.0 | $-326.81 | -18.9% | $673.19 | -2.5 | Wed 5:00 PM | too few trades (173/200) |
| always_up | 356 | 46.1 | 50.1 | $-398.65 | -11.2% | $601.35 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 492 | 48.0 | 49.9 | $-166.04 |
| ETH | 563 | 46.9 | 48.7 | $-326.66 |
| SOL | 620 | 49.8 | 48.6 | $-222.18 |
| XRP | 636 | 49.7 | 48.8 | $-349.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
