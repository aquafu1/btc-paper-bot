# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1352 windows, 35420 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 699 | 34.2 | 35.4 | $-551.96 | -7.9% | $448.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1708 | 38.7 | 39.2 | $-837.95 | -4.9% | $162.05 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3541 | 50.9 | 50.1 | $-1014.41 | -2.9% | $-14.41 | -1.7 | done | can't tell from luck |
| value_ev5 | 2580 | 40.4 | 41.1 | $-1333.61 | -5.2% | $-333.61 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2978 | 49.4 | 49.5 | $-1456.17 | -4.9% | $-456.17 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2978 | 50.6 | 50.9 | $-1553.00 | -5.2% | $-553.00 | -2.9 | done | losing for real |
| trend_filter | 2107 | 48.6 | 50.5 | $-1839.16 | -8.7% | $-839.16 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3541 | 49.1 | 50.3 | $-2239.90 | -6.3% | $-1239.90 | -3.8 | done | losing for real |
| coinflip | 5096 | 49.9 | 50.1 | $-2339.31 | -4.6% | $-1339.31 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5096 | 50.2 | 51.3 | $-3060.28 | -6.0% | $-2060.28 | -4.4 | done | losing for real |
| always_up | 5096 | 47.9 | 49.3 | $-3695.72 | -7.3% | $-2695.72 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8713 | 47.8 | 48.8 | $-5290.36 |
| ETH | 9397 | 48.1 | 48.2 | $-5046.87 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
