# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1036 windows, 28780 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 534 | 34.8 | 35.1 | $-264.76 | -5.0% | $735.24 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2928 | 51.2 | 50.5 | $-802.04 | -2.7% | $197.96 | -1.5 | done | can't tell from luck |
| value_ev10 | 1325 | 37.5 | 39.2 | $-976.31 | -7.4% | $23.69 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2465 | 49.7 | 49.6 | $-1122.65 | -4.6% | $-122.65 | -2.3 | done | losing for real |
| trend_filter | 1721 | 49.3 | 50.7 | $-1341.06 | -7.8% | $-341.06 | -3.3 | done | losing for real |
| value_ev5 | 2006 | 39.5 | 41.0 | $-1388.69 | -6.9% | $-388.69 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2465 | 50.3 | 51.0 | $-1602.60 | -6.5% | $-602.60 | -3.3 | done | losing for real |
| coinflip | 4136 | 50.5 | 50.3 | $-1640.34 | -4.0% | $-640.34 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2928 | 48.8 | 50.2 | $-2032.96 | -6.9% | $-1032.96 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4136 | 50.7 | 51.5 | $-2305.26 | -5.6% | $-1305.26 | -3.7 | done | losing for real |
| always_up | 4136 | 47.4 | 49.5 | $-3583.77 | -8.7% | $-2583.77 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6565 | 48.2 | 49.0 | $-3666.04 |
| ETH | 7136 | 48.2 | 48.5 | $-4397.88 |
| SOL | 7514 | 48.2 | 48.6 | $-4308.03 |
| XRP | 7565 | 48.1 | 48.3 | $-4688.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
