# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 936 windows, 25876 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1168 | 38.0 | 39.1 | $-683.12 | -5.8% | $316.88 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2644 | 50.9 | 50.6 | $-907.56 | -3.4% | $92.44 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2210 | 50.1 | 49.8 | $-952.47 | -4.3% | $47.53 | -2.0 | done | losing for real |
| trend_filter | 1539 | 50.0 | 51.0 | $-1050.73 | -6.8% | $-50.73 | -2.8 | done | losing for real |
| value_ev5 | 1777 | 39.7 | 41.0 | $-1129.62 | -6.4% | $-129.62 | -2.3 | done | losing for real |
| coinflip | 3736 | 50.5 | 50.4 | $-1509.94 | -4.0% | $-509.94 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2210 | 49.9 | 50.9 | $-1529.31 | -6.9% | $-529.31 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2644 | 49.1 | 50.3 | $-1681.55 | -6.4% | $-681.55 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3736 | 51.0 | 51.6 | $-1861.57 | -5.0% | $-861.57 | -3.1 | done | losing for real |
| always_up | 3736 | 46.8 | 49.7 | $-3834.32 | -10.3% | $-2834.32 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5899 | 48.2 | 49.1 | $-3460.30 |
| ETH | 6433 | 48.2 | 48.6 | $-4020.34 |
| SOL | 6751 | 48.2 | 48.6 | $-3943.17 |
| XRP | 6793 | 48.3 | 48.5 | $-3872.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
