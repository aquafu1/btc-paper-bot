# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1140 windows, 31502 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 607 | 34.6 | 35.2 | $-382.50 | -6.3% | $617.50 | -1.2 | done | can't tell from luck |
| value_ev10 | 1477 | 38.1 | 39.2 | $-928.98 | -6.3% | $71.02 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3169 | 50.9 | 50.4 | $-971.62 | -3.1% | $28.38 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2660 | 49.7 | 49.4 | $-1153.41 | -4.3% | $-153.41 | -2.2 | done | losing for real |
| value_ev5 | 2234 | 40.1 | 41.1 | $-1311.19 | -5.9% | $-311.19 | -2.4 | done | losing for real |
| trend_filter | 1870 | 49.0 | 50.5 | $-1470.56 | -7.9% | $-470.56 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2660 | 50.3 | 51.1 | $-1660.91 | -6.2% | $-660.91 | -3.3 | done | losing for real |
| coinflip | 4552 | 50.3 | 50.2 | $-1892.06 | -4.2% | $-892.06 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3169 | 49.1 | 50.2 | $-1982.08 | -6.3% | $-982.08 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4552 | 50.2 | 51.4 | $-2819.21 | -6.2% | $-1819.21 | -4.3 | done | losing for real |
| always_up | 4552 | 47.7 | 49.3 | $-3441.47 | -7.6% | $-2441.47 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7217 | 48.3 | 49.0 | $-3740.57 |
| ETH | 7806 | 48.2 | 48.4 | $-4632.71 |
| SOL | 8202 | 48.0 | 48.4 | $-4627.14 |
| XRP | 8277 | 48.1 | 48.2 | $-5013.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
