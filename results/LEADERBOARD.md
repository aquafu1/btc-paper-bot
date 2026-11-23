# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1158 windows, 32019 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 617 | 34.7 | 35.3 | $-372.55 | -6.0% | $627.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1510 | 38.3 | 39.2 | $-851.46 | -5.6% | $148.54 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3214 | 50.7 | 50.4 | $-1088.55 | -3.4% | $-88.55 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2701 | 49.8 | 49.5 | $-1125.78 | -4.2% | $-125.78 | -2.2 | done | losing for real |
| value_ev5 | 2283 | 40.3 | 41.1 | $-1239.26 | -5.4% | $-239.26 | -2.2 | done | losing for real |
| trend_filter | 1898 | 49.1 | 50.5 | $-1486.88 | -7.8% | $-486.88 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2701 | 50.2 | 51.0 | $-1729.04 | -6.4% | $-729.04 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3214 | 49.3 | 50.2 | $-1892.92 | -5.9% | $-892.92 | -3.4 | done | losing for real |
| coinflip | 4627 | 50.2 | 50.2 | $-1954.29 | -4.2% | $-954.29 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4627 | 50.1 | 51.4 | $-2886.46 | -6.2% | $-1886.46 | -4.4 | done | losing for real |
| always_up | 4627 | 47.8 | 49.3 | $-3434.80 | -7.4% | $-2434.80 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7341 | 48.2 | 49.0 | $-3820.92 |
| ETH | 7940 | 48.2 | 48.4 | $-4609.52 |
| SOL | 8337 | 48.1 | 48.4 | $-4545.22 |
| XRP | 8401 | 48.1 | 48.2 | $-5086.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
