# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 92 windows, 2333 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 360 | 55.6 | 50.9 | $+211.76 | +5.9% | $1211.76 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 174 | 58.6 | 52.7 | $+146.43 | +8.4% | $1146.43 | +1.2 | Wed 5:15 PM | too few trades (174/200) |
| reversal_15m_0.10pct | 225 | 56.4 | 52.4 | $+124.18 | +5.5% | $1124.18 | +0.9 | done | can't tell from luck |
| value_ev10 | 119 | 41.2 | 40.2 | $-33.12 | -2.8% | $966.88 | -0.3 | Thu 5:15 AM | too few trades (119/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 9:45 PM | too few trades (44/200) |
| trend_filter | 127 | 47.2 | 48.8 | $-84.96 | -6.7% | $915.04 | -0.7 | Thu 2:45 AM | too few trades (127/200) |
| value_ev5 | 165 | 38.8 | 41.7 | $-178.55 | -10.8% | $821.45 | -1.2 | Wed 6:45 PM | too few trades (165/200) |
| coinflip | 360 | 50.0 | 51.6 | $-231.78 | -6.4% | $768.22 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 174 | 41.4 | 49.0 | $-318.56 | -18.3% | $681.44 | -2.4 | Wed 5:15 PM | too few trades (174/200) |
| momentum_15m_0.10pct | 225 | 43.6 | 49.5 | $-332.32 | -14.8% | $667.68 | -2.2 | done | losing for real |
| always_up | 360 | 45.6 | 50.1 | $-438.65 | -12.2% | $561.35 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 497 | 47.7 | 49.9 | $-198.73 |
| ETH | 568 | 46.7 | 48.7 | $-360.20 |
| SOL | 627 | 49.6 | 48.6 | $-258.78 |
| XRP | 641 | 49.5 | 48.8 | $-381.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
