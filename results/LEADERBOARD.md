# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 90 windows, 2284 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 352 | 56.0 | 50.9 | $+232.48 | +6.6% | $1232.48 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 170 | 58.2 | 52.8 | $+127.15 | +7.5% | $1127.15 | +1.0 | Wed 5:15 PM | too few trades (170/200) |
| reversal_15m_0.10pct | 218 | 55.0 | 52.4 | $+64.35 | +3.0% | $1064.35 | +0.5 | done | can't tell from luck |
| value_ev10 | 118 | 41.5 | 40.2 | $-23.12 | -2.0% | $976.88 | -0.2 | Thu 4:45 AM | too few trades (118/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 7:15 PM | too few trades (44/200) |
| trend_filter | 126 | 47.6 | 48.8 | $-74.96 | -5.9% | $925.04 | -0.6 | Thu 2:15 AM | too few trades (126/200) |
| value_ev5 | 164 | 39.0 | 41.7 | $-168.55 | -10.3% | $831.45 | -1.1 | Wed 6:15 PM | too few trades (164/200) |
| coinflip | 352 | 50.3 | 51.6 | $-208.27 | -5.9% | $791.73 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 218 | 45.0 | 49.4 | $-262.32 | -12.0% | $737.68 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 170 | 41.8 | 48.9 | $-296.81 | -17.5% | $703.19 | -2.3 | Wed 5:15 PM | too few trades (170/200) |
| always_up | 352 | 45.5 | 50.1 | $-438.00 | -12.4% | $562.00 | -2.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 486 | 48.1 | 49.8 | $-146.19 |
| ETH | 556 | 46.8 | 48.7 | $-334.63 |
| SOL | 613 | 49.6 | 48.5 | $-248.68 |
| XRP | 629 | 49.4 | 48.8 | $-382.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
