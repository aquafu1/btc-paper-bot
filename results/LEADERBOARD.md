# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1305 windows, 34749 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 685 | 34.3 | 35.3 | $-510.82 | -7.5% | $489.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1675 | 38.8 | 39.2 | $-767.85 | -4.6% | $232.15 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3486 | 50.8 | 50.2 | $-1055.39 | -3.0% | $-55.39 | -1.8 | done | can't tell from luck |
| value_ev5 | 2527 | 40.5 | 41.1 | $-1234.55 | -4.9% | $-234.55 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2915 | 49.4 | 49.4 | $-1369.97 | -4.7% | $-369.97 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2915 | 50.6 | 51.0 | $-1575.51 | -5.4% | $-575.51 | -3.0 | done | losing for real |
| trend_filter | 2060 | 48.8 | 50.5 | $-1717.04 | -8.3% | $-717.04 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3486 | 49.2 | 50.2 | $-2152.99 | -6.2% | $-1152.99 | -3.7 | done | losing for real |
| coinflip | 5000 | 50.0 | 50.1 | $-2237.28 | -4.5% | $-1237.28 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5000 | 50.4 | 51.4 | $-2903.57 | -5.8% | $-1903.57 | -4.2 | done | losing for real |
| always_up | 5000 | 47.9 | 49.3 | $-3609.41 | -7.2% | $-2609.41 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8393 | 48.0 | 48.8 | $-4857.29 |
| ETH | 9046 | 48.2 | 48.2 | $-4692.84 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
