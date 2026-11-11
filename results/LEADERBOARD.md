# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 89 windows, 2277 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 351 | 56.1 | 50.9 | $+242.48 | +6.9% | $1242.48 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 169 | 58.6 | 52.8 | $+137.15 | +8.1% | $1137.15 | +1.1 | Wed 5:30 PM | too few trades (169/200) |
| reversal_15m_0.10pct | 217 | 55.3 | 52.4 | $+74.35 | +3.4% | $1074.35 | +0.5 | done | can't tell from luck |
| value_ev10 | 118 | 41.5 | 40.2 | $-23.12 | -2.0% | $976.88 | -0.2 | Thu 4:45 AM | too few trades (118/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 7:15 PM | too few trades (44/200) |
| trend_filter | 126 | 47.6 | 48.8 | $-74.96 | -5.9% | $925.04 | -0.6 | Thu 2:15 AM | too few trades (126/200) |
| value_ev5 | 164 | 39.0 | 41.7 | $-168.55 | -10.3% | $831.45 | -1.1 | Wed 6:15 PM | too few trades (164/200) |
| coinflip | 351 | 50.1 | 51.6 | $-220.10 | -6.3% | $779.90 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 217 | 44.7 | 49.5 | $-274.15 | -12.6% | $725.85 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 169 | 41.4 | 48.9 | $-308.64 | -18.3% | $691.36 | -2.4 | Wed 5:30 PM | too few trades (169/200) |
| always_up | 351 | 45.6 | 50.1 | $-428.00 | -12.2% | $572.00 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 486 | 48.1 | 49.8 | $-146.19 |
| ETH | 556 | 46.8 | 48.7 | $-334.63 |
| SOL | 606 | 49.7 | 48.5 | $-244.19 |
| XRP | 629 | 49.4 | 48.8 | $-382.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
