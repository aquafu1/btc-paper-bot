# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1094 windows, 30276 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 571 | 34.7 | 35.0 | $-310.36 | -5.4% | $689.64 | -1.0 | done | can't tell from luck |
| value_ev10 | 1403 | 38.1 | 39.1 | $-824.39 | -5.9% | $175.61 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3057 | 51.0 | 50.5 | $-915.81 | -3.0% | $84.19 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2577 | 49.6 | 49.4 | $-1124.77 | -4.4% | $-124.77 | -2.2 | done | losing for real |
| value_ev5 | 2132 | 40.1 | 41.0 | $-1174.00 | -5.5% | $-174.00 | -2.1 | done | losing for real |
| trend_filter | 1798 | 49.3 | 50.5 | $-1321.80 | -7.4% | $-321.80 | -3.2 | done | losing for real |
| coinflip | 4368 | 50.6 | 50.2 | $-1587.22 | -3.6% | $-587.22 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2577 | 50.4 | 51.1 | $-1622.59 | -6.3% | $-622.59 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3057 | 49.0 | 50.2 | $-1966.11 | -6.4% | $-966.11 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4368 | 50.8 | 51.4 | $-2207.30 | -5.1% | $-1207.30 | -3.4 | done | losing for real |
| always_up | 4368 | 47.5 | 49.3 | $-3478.32 | -8.0% | $-2478.32 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6923 | 48.5 | 49.0 | $-3354.98 |
| ETH | 7502 | 48.2 | 48.4 | $-4344.42 |
| SOL | 7889 | 48.1 | 48.4 | $-4377.53 |
| XRP | 7962 | 48.3 | 48.2 | $-4455.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
