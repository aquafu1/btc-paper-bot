# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 94 windows, 2389 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 368 | 56.0 | 51.0 | $+234.74 | +6.4% | $1234.74 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 177 | 58.8 | 52.8 | $+152.03 | +8.6% | $1152.03 | +1.2 | Wed 5:15 PM | too few trades (177/200) |
| reversal_15m_0.10pct | 230 | 56.1 | 52.4 | $+109.78 | +4.8% | $1109.78 | +0.8 | done | can't tell from luck |
| value_ev10 | 125 | 40.0 | 40.4 | $-73.04 | -5.8% | $926.96 | -0.6 | Thu 4:15 AM | too few trades (125/200) |
| value_ev20 | 47 | 29.8 | 36.4 | $-93.85 | -20.0% | $906.15 | -1.1 | Sat 5:15 PM | too few trades (47/200) |
| trend_filter | 128 | 46.9 | 48.9 | $-94.96 | -7.4% | $905.04 | -0.8 | Thu 3:15 AM | too few trades (128/200) |
| coinflip | 368 | 50.8 | 51.6 | $-186.09 | -5.1% | $813.91 | -1.0 | done | can't tell from luck |
| value_ev5 | 171 | 38.0 | 41.8 | $-218.48 | -12.8% | $781.52 | -1.5 | Wed 6:15 PM | too few trades (171/200) |
| momentum_60m_0.30pct | 177 | 41.2 | 49.0 | $-328.49 | -18.6% | $671.51 | -2.5 | Wed 5:15 PM | too few trades (177/200) |
| momentum_15m_0.10pct | 230 | 43.9 | 49.5 | $-328.50 | -14.3% | $671.50 | -2.2 | done | losing for real |
| always_up | 368 | 46.5 | 50.2 | $-397.08 | -10.8% | $602.92 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 506 | 47.8 | 49.8 | $-196.61 |
| ETH | 583 | 46.8 | 48.8 | $-361.23 |
| SOL | 642 | 49.7 | 48.6 | $-268.71 |
| XRP | 658 | 49.5 | 48.9 | $-397.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
