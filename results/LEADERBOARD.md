# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 127 windows, 3212 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 234 | 62.0 | 53.1 | $+336.30 | +14.4% | $1336.30 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 304 | 56.6 | 52.0 | $+194.62 | +6.4% | $1194.62 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 500 | 52.4 | 50.8 | $-63.05 | -1.3% | $936.95 | -0.3 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 6:00 AM | too few trades (61/200) |
| value_ev10 | 168 | 37.5 | 40.4 | $-194.30 | -11.6% | $805.70 | -1.3 | Thu 7:30 AM | too few trades (168/200) |
| coinflip | 500 | 50.6 | 51.0 | $-274.41 | -5.5% | $725.59 | -1.3 | done | can't tell from luck |
| trend_filter | 168 | 41.1 | 48.9 | $-321.43 | -19.1% | $678.57 | -2.5 | Thu 7:30 AM | too few trades (168/200) |
| value_ev5 | 239 | 37.2 | 41.9 | $-359.45 | -15.0% | $640.55 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 304 | 43.4 | 50.1 | $-491.98 | -16.2% | $508.02 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 234 | 38.0 | 49.1 | $-577.49 | -24.7% | $422.51 | -3.8 | done | losing for real |
| always_up | 500 | 45.6 | 50.2 | $-677.28 | -13.5% | $322.72 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 690 | 45.1 | 49.5 | $-791.36 |
| ETH | 791 | 44.8 | 48.7 | $-941.35 |
| SOL | 852 | 48.5 | 48.6 | $-569.17 |
| XRP | 879 | 50.1 | 49.0 | $-309.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
