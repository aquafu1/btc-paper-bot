# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 78 windows, 1952 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 304 | 56.9 | 50.9 | $+250.27 | +8.2% | $1250.27 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 140 | 60.7 | 52.7 | $+177.77 | +12.7% | $1177.77 | +1.6 | Wed 6:30 PM | too few trades (140/200) |
| reversal_15m_0.10pct | 183 | 57.4 | 52.0 | $+142.41 | +7.8% | $1142.41 | +1.1 | Wed 12:15 PM | too few trades (183/200) |
| value_ev10 | 105 | 41.0 | 39.8 | $-30.48 | -2.9% | $969.52 | -0.2 | Thu 3:30 AM | too few trades (105/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 7:45 AM | too few trades (43/200) |
| trend_filter | 102 | 46.1 | 48.6 | $-88.59 | -8.7% | $911.41 | -0.8 | Thu 4:45 AM | too few trades (102/200) |
| value_ev5 | 144 | 39.6 | 41.3 | $-128.07 | -8.9% | $871.93 | -0.9 | Wed 5:45 PM | too few trades (144/200) |
| coinflip | 304 | 50.0 | 51.5 | $-198.87 | -6.5% | $801.13 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 140 | 39.3 | 48.6 | $-302.11 | -21.6% | $697.89 | -2.5 | Wed 6:30 PM | too few trades (140/200) |
| momentum_15m_0.10pct | 183 | 42.6 | 49.4 | $-305.57 | -16.7% | $694.42 | -2.3 | Wed 12:15 PM | too few trades (183/200) |
| always_up | 304 | 44.7 | 50.2 | $-431.68 | -14.2% | $568.32 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 412 | 47.3 | 49.8 | $-161.14 |
| ETH | 468 | 46.6 | 48.6 | $-293.81 |
| SOL | 528 | 48.9 | 48.2 | $-298.11 |
| XRP | 544 | 50.4 | 48.3 | $-215.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
