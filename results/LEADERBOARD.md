# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 434 windows, 11923 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 218 | 33.9 | 36.1 | $-214.42 | -9.8% | $785.58 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1014 | 50.8 | 50.0 | $-270.87 | -2.7% | $729.13 | -0.9 | done | can't tell from luck |
| trend_filter | 684 | 49.9 | 50.7 | $-400.80 | -5.9% | $599.20 | -1.6 | done | can't tell from luck |
| value_ev10 | 560 | 38.8 | 40.2 | $-415.64 | -7.4% | $584.36 | -1.5 | done | can't tell from luck |
| value_ev5 | 837 | 41.1 | 42.0 | $-501.13 | -6.0% | $498.87 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1206 | 49.4 | 50.1 | $-602.27 | -5.0% | $397.73 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1206 | 50.6 | 51.6 | $-768.85 | -6.4% | $231.15 | -2.3 | done | losing for real |
| coinflip | 1728 | 50.5 | 50.9 | $-795.03 | -4.6% | $204.97 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1014 | 49.2 | 51.8 | $-937.25 | -9.2% | $62.75 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1728 | 49.7 | 51.6 | $-1257.58 | -7.3% | $-257.58 | -3.1 | done | losing for real |
| always_up | 1728 | 46.1 | 50.4 | $-2147.59 | -12.4% | $-1147.59 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2692 | 47.5 | 49.3 | $-2087.86 |
| ETH | 2992 | 48.0 | 48.9 | $-1944.54 |
| SOL | 3096 | 47.8 | 49.3 | $-2468.83 |
| XRP | 3143 | 48.6 | 49.3 | $-1810.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
