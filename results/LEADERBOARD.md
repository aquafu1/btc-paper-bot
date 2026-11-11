# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 82 windows, 2078 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 322 | 57.1 | 50.9 | $+287.94 | +8.9% | $1287.94 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 150 | 59.3 | 52.8 | $+149.60 | +10.0% | $1149.60 | +1.3 | Wed 6:15 PM | too few trades (150/200) |
| reversal_15m_0.10pct | 196 | 57.1 | 52.1 | $+149.52 | +7.6% | $1149.52 | +1.1 | Wed 12:00 PM | too few trades (196/200) |
| value_ev10 | 113 | 42.5 | 40.1 | $+2.34 | +0.2% | $1002.34 | +0.0 | Thu 3:15 AM | too few trades (113/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 1:30 PM | too few trades (43/200) |
| trend_filter | 111 | 47.7 | 48.8 | $-58.97 | -5.3% | $941.03 | -0.5 | Thu 3:45 AM | too few trades (111/200) |
| value_ev5 | 153 | 41.2 | 41.5 | $-83.10 | -5.4% | $916.90 | -0.6 | Wed 5:45 PM | too few trades (153/200) |
| coinflip | 322 | 50.3 | 51.5 | $-178.29 | -5.5% | $821.71 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 150 | 40.7 | 48.7 | $-284.18 | -18.9% | $715.82 | -2.3 | Wed 6:15 PM | too few trades (150/200) |
| momentum_15m_0.10pct | 196 | 42.9 | 49.5 | $-315.93 | -16.1% | $684.07 | -2.3 | Wed 12:00 PM | too few trades (196/200) |
| always_up | 322 | 46.3 | 50.1 | $-344.52 | -10.7% | $655.48 | -1.9 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 445 | 47.9 | 49.8 | $-126.68 |
| ETH | 497 | 47.3 | 48.6 | $-230.56 |
| SOL | 560 | 50.4 | 48.3 | $-117.94 |
| XRP | 576 | 50.2 | 48.5 | $-254.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
